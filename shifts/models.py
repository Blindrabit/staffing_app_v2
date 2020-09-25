from django.db import models
from django.conf import settings

class Shifts(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    manage = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    def __str__(self):
        return self.start_time +" - "+self.end_time
