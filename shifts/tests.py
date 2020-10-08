import factory
from django.test import TestCase, Client
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model
from django.db.models import signals

from .models import Shifts
from users.models import HospitalListModel

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
        self.shifts = Shifts.objects.create(
                manage=None,  
                hospital=self.hospital,
                start_time='2020-09-30 08:00:00+00:00',
                end_time='2020-09-30 17:00:00+00:00',
            )
        
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
        self.assertEqual(response.status_code, 302)

    def test_shifts_list_view_logged_out(self):
        response = self.client.get(reverse('shiftlist'))
        self.assertEqual(response.status_code, 302)



class ShiftsModelSignalTests(TestCase):

    def setUp(self):
        self.shifts = Shifts.objects.create(
                manage=None,  
                hospital=self.hospital,
                start_time='2020-09-30 08:00:00+00:00',
                end_time='2020-09-30 17:00:00+00:00',
            )
    


        