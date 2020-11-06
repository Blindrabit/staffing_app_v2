from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from calendar_app.models import Event
from django.contrib.auth import get_user_model
from shifts.models import Shifts
from users.models import HospitalListModel, AreaToWorkModel

class ShiftAPITest(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'test_username', 
            email = 'test_username@example.com', 
            password = 'da_password',
            ) 
        self.client.force_authenticate(user=self.user)
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
    def test_shift_list_api_url(self):
        url = reverse('api-shift-list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_shift_create_api_url(self):
        url = reverse('api-shift-create')
        data = { 'manage' : None,  
                'hospital' : self.hospital.id,
                'area' : self.area.id,
                'start_time' : '2020-09-30 08:00:00+00:00',
                'end_time' :'2020-09-30 17:00:00+00:00',
        }
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, 201)
        self.assertEquals(Shifts.objects.count(), 2)

    def test_shift_detail_update_api_url(self):
        url = f'/api/v1/shifts/{self.shifts.id}/'
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        data = { 'manage' : None,  
                'hospital' : self.hospital.id,
                'area' : self.area.id,
                'start_time' : '2020-09-30 08:00:00+00:00',
                'end_time' :'2020-09-30 18:00:00+00:00',
        }
        response = self.client.put(url, data, format='json')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['end_time'], '2020-09-30T18:00:00Z')

class CalendarAPITests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'test_username', 
            email = 'test_username@example.com', 
            password = 'da_password',
            ) 
        self.client.force_authenticate(user=self.user)
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
        self.eventbooked = Event.objects.create(
            manage=self.user,  
            availability='Booked',
            start_time='2020-09-30 08:00:00+00:00',
            end_time='2020-09-30 17:00:00+00:00',
            )

    def test_calendar_list_api(self):
        url = reverse('api-calendar-list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
    
    def test_calendar_create_api(self):
        url =  reverse('api-calendar-create')
        data = {'manage' : self.user.id,  
            'availability' : 'Busy',
            'start_time' : '2020-09-30 08:00:00+00:00',
            'end_time' : '2020-09-30 17:00:00+00:00',
        }
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, 201)
        self.assertEquals(Event.objects.count(), 2)
    
    def test_calendar_detail_update_api(self):
        url = f'/api/v1/calendar/{self.eventbooked.id}/'
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        data = {'manage' : self.user.id,  
            'availability' : 'Busy',
            'start_time' : '2020-09-30 08:00:00+00:00',
            'end_time' : '2020-09-30 18:00:00+00:00',
            }
        response = self.client.put(url, data, format='json')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['end_time'], '2020-09-30T18:00:00Z')