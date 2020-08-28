from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTests(TestCase):

    def test_user_create(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='AdamTest',
            email='Adamtest@email.co.uk',
            password='testpass123'
        )

        self.assertEqual(user.username, 'AdamTest')
        self.assertEqual(user.email, 'Adamtest@email.co.uk')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_superuser_create(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='superuser',
            email='superuser@email.co.uk',
            password='testpass123'
        )

        self.assertEqual(user.username, 'superuser')
        self.assertEqual(user.email, 'superuser@email.co.uk')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)