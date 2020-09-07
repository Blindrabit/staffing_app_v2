import uuid
from django.db import models
from django.contrib.auth import get_user_model




class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    manage = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    avilibility = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.avilibility + " - " + str(self.start_time) + " - " + str(self.end_time)