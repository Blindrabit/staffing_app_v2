from django.test import SimpleTestCase
from django.urls import resolve, reverse

from .views import HomePageView


class HomePageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_name_url(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'home.html')
        self.assertContains(self.response, 'Homepage')
        self.assertNotContains(self.response, 'This should be there!')
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)
