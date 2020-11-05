from django.urls import reverse
from rest_framwork import status
from rest_framework.tests import APITestCase

from shifts.models import Shifts

class ShiftCreateTest(APITestCase):
    url = reverse('api-shift-create')
    data = {'manage=':  None,
            'hospital': self.hospital,
            area=self.area,
            start_time='2020-09-30 08:00:00+00:00',
            end_time='2020-09-30 17:00:00+00:00','}