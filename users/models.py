from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    dbs_number = models.CharField(max_length=13, default="DBS_num_place")
    
