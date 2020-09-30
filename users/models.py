import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models


class HospitalListModel(models.Model):
    hospital = models.CharField(max_length=100)

    def __str__(self):
        return self.hospital

class CustomUser(AbstractUser):
    dbs_number = models.CharField(max_length=13, default="DBS_num_place")
    hospitals = models.ManyToManyField(HospitalListModel, verbose_name=('hospital'), blank=True)
    




    


