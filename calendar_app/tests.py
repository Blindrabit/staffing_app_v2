from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Event

class EventTests(TestCase):
    
    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user(
            'test_username', 
            'test_username@example.com', 
            'da_password') 
        self.event = Event.objects.create(
            manage=user,  
            avilibility='Booked',
            start_time='2020-09-30 08:00:00+00:00',
            end_time='2020-09-30 17:00:00+00:00',
        )

    def test_event_create(self):
        self.assertEquals(f'{self.event.manage}', 'test_username')
        self.assertEquals(f'{self.event.start_time}','2020-09-30 08:00:00+00:00')
        self.assertEquals(f'{self.event.end_time}','2020-09-30 17:00:00+00:00')

    def test_calendar_list_view(self):
        response = self.client.get(reverse('calendar_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'calendar_list.html')
    
    def test_event_detail_view(self):
        response = self.client.get(self.event.get_absolute_url())
        no_response = self.client.get('/calendar/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Booked')