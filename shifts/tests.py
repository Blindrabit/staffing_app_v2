from datetime import date, datetime, timedelta

import factory
from django.contrib.auth import get_user_model
from django.db.models import signals
from django.forms import ValidationError
from django.test import Client, TestCase
from django.urls import reverse, reverse_lazy

from calendar_app.models import Event
from users.models import AreaToWorkModel, HospitalListModel

from .forms import ShiftForm
from .models import Shifts
from .tasks import autoshiftandeventmatching


class ShiftsTests(TestCase):
    @factory.django.mute_signals(signals.post_save)
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'test_username', 
            email = 'test_username@example.com', 
            password = 'da_password',
            ) 
        self.hospital = HospitalListModel.objects.create(
            hospital= 'test hospital',
            )
        self.area = AreaToWorkModel.objects.create(
            area = 'test_area',
            )
        self.shifts = Shifts.objects.create(
                manage=None,  
                hospital=self.hospital,
                area=self.area,
                start_time='2020-09-30 08:00:00+00:00',
                end_time='2020-09-30 17:00:00+00:00',
            )
        self.bad_data = {
            'hospital' : self.hospital,
            'start_time' : '2020-09-30 18:00:00+00:00',
            'end_time' : '2020-09-30 17:00:00+00:00',
        }
        
    def test_shifts_create(self):
        self.assertEqual(f'{self.shifts.manage}', 'None')
        self.assertEqual(f'{self.shifts.hospital}', 'test hospital')
        self.assertEqual(f'{self.shifts.start_time}','2020-09-30 08:00:00+00:00')
        self.assertEqual(f'{self.shifts.end_time}','2020-09-30 17:00:00+00:00')

    def test_shifts_list_view(self):
        self.client.login(email='test_username@example.com', password='da_password')
        response = self.client.get(reverse('shiftlist'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shiftlist.html')

    def test_shifts_detail_view(self):
        self.client.login(email='test_username@example.com', password='da_password')
        response = self.client.get(reverse('createshift'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shiftcreate.html')

    def test_shifts_create_view_logged_out(self):
        response = self.client.get(reverse('createshift'))
        self.assertRedirects(response, '/accounts/login/?next=/shifts/create/', status_code=302, target_status_code=200)

    def test_shifts_list_view_logged_out(self):
        response = self.client.get(reverse('shiftlist'))
        self.assertRedirects(response, '/accounts/login/?next=/shifts/all/', status_code=302, target_status_code=200)
    
    def test_start_time_greater_than_end_time_validation_error(self):
        form = ShiftForm(self.bad_data)
        self.assertFalse(form.is_valid())
        self.assertRaises(ValidationError)



class ShiftsModelSignalandAutoBookingTests(TestCase):

    def setUp(self):
        self.hospital = HospitalListModel.objects.create(
            hospital= 'test hospital',
            )
        self.area = AreaToWorkModel.objects.create(
            area = 'test_area',
        )
        self.user = get_user_model().objects.create_user(
            username = 'test_username', 
            email = 'test_username@example.com', 
            password = 'da_password',
            ) 
        self.user.hospitals.add(self.hospital)
        self.user.area_to_work.add(self.area)
        self.event = Event.objects.create(
            manage=self.user,
            availability='Available',
            start_time=f'{date.today()+timedelta(days=10)} 07:00:00+00:00',
            end_time=f'{date.today()+timedelta(days=10)} 18:00:00+00:00',
            )
        self.shifts = Shifts.objects.create(
            manage=None,  
            hospital=self.hospital,
            area=self.area,
            start_time=f'{date.today()+timedelta(days=10)} 08:00:00+00:00',
            end_time=f'{date.today()+timedelta(days=10)} 17:00:00+00:00',
            )

    def test_autobooking_feature(self):
        autoshiftandeventmatching()
        self.event.refresh_from_db()
        self.shifts.refresh_from_db()
        self.assertEqual(f'{self.event.availability}', 'Booked')
        self.assertEqual(f'{self.event.start_time}', f'{date.today()+timedelta(days=10)} 08:00:00+00:00')
        self.assertEqual(f'{self.event.end_time}', f'{date.today()+timedelta(days=10)} 17:00:00+00:00')
        self.assertEqual(f'{self.event.hospital}', f'{self.shifts.hospital}')
        self.assertEqual(f'{self.event.area}', f'{self.shifts.area}')
        self.assertEqual(f'{self.shifts.manage}', self.user.username)

        
  