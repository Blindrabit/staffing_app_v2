from django.contrib.auth import get_user_model
from django.forms import ValidationError
from django.test import Client, TestCase
from django.urls import reverse, reverse_lazy

from .forms import EventForm
from .models import Event


class EventTests(TestCase):
    
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'test_username', 
            email = 'test_username@example.com', 
            password = 'da_password') 
        self.event = Event.objects.create(
            manage=self.user,  
            availability='Available',
            start_time='2020-09-30 08:00:00+00:00',
            end_time='2020-09-30 17:00:00+00:00',
        )
        self.eventbooked = Event.objects.create(
            manage=self.user,  
            availability='Booked',
            start_time='2020-09-30 08:00:00+00:00',
            end_time='2020-09-30 17:00:00+00:00',
        )
        self.bad_data = {
            'manage':self.user,
            'availability': 'available',
            'start_time' : '2020-09-30 18:00:00+00:00',
            'end_time' : '2020-09-30 17:00:00+00:00',
        }

    def test_event_create(self):
        self.assertEqual(f'{self.event.manage}', 'test_username')
        self.assertEqual(f'{self.event.availability}', 'Available')
        self.assertEqual(f'{self.event.start_time}','2020-09-30 08:00:00+00:00')
        self.assertEqual(f'{self.event.end_time}','2020-09-30 17:00:00+00:00')

    def test_calendar_list_view(self):
        self.client.login(email='test_username@example.com', password='da_password')
        response = self.client.get(reverse('calendar_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'calendar_list.html')
    
    def test_event_detail_view(self):
        self.client.login(email='test_username@example.com', password='da_password')
        response = self.client.get(self.event.get_absolute_url())
        no_response = self.client.get('/calendar/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Available')

    def test_event_create_view_logged_in(self):
        self.client.login(email='test_username@example.com', password='da_password')
        response = self.client.get(reverse('event_add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'calendar_create_event_form.html')

    def test_event_create_view_logged_out(self):
        response = self.client.get(reverse('event_add'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/calendar/create/', status_code=302, target_status_code=200)

    def test_event_update_view(self):
        self.client.login(email='test_username@example.com', password='da_password')
        response = self.client.get(self.event.get_absolute_url_edit())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Update Availability')

    def test_event_update_redirect_if_booked_view(self):
        self.client.login(email='test_username@example.com', password='da_password')
        response = self.client.get(self.eventbooked.get_absolute_url_edit())
        self.assertRedirects(response, reverse('calendar_list'), status_code=302, target_status_code=200)

    def test_event_calendar_view(self):
        self.client.login(email='test_username@example.com', password='da_password')
        response = self.client.get(reverse('calendar'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'calendar.html')
    
    def test_start_time_greater_than_end_time_validation_error(self):
        form = EventForm(self.bad_data)
        self.assertFalse(form.is_valid())
        self.assertRaises(ValidationError)