from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

from .forms import MyCustomSignupForm

class CustomUserTests(TestCase):

    def test_user_create(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='AdamTest',
            email='Adamtest@email.co.uk',
            password='testpass123',
            dbs_number='1234567890123'
        )

        self.assertEqual(user.username, 'AdamTest')
        self.assertEqual(user.email, 'Adamtest@email.co.uk')
        self.assertEquals(user.dbs_number, '1234567890123')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_superuser_create(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='superuser',
            email='superuser@email.co.uk',
            password='testpass123',
            dbs_number='1234567890123'
        )

        self.assertEqual(user.username, 'superuser')
        self.assertEqual(user.email, 'superuser@email.co.uk')
        self.assertEquals(user.dbs_number, '1234567890123')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

class SignUpPageTests(TestCase):

    username = 'newuser'
    email = 'newuser@email.com'

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'This should not be there')

    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, MyCustomSignupForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')
        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)

