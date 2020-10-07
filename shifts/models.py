from django.db import models
from django.conf import settings

from users.models import HospitalListModel

class Shifts(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    hospital = models.ForeignKey(HospitalListModel, on_delete=models.CASCADE, default= None)
    manage = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return str(self.start_time) +" - "+ str(self.end_time)