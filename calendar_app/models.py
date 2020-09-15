import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Event(models.Model):

    avilibility_choices = [
        ('Avilible', 'Avilible'),
        ('Busy', 'Busy'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    manage = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    avilibility = models.CharField(max_length=10, choices=avilibility_choices, editable=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.avilibility + " - " + str(self.start_time) + " - " + str(self.end_time) + " - " +str(self.id)

    def get_absolute_url(self):
        return reverse('calendar_event_detail', args=[str(self.id)])

    def get_absolute_url_edit(self):
        return reverse('calendar_event_detail_update', args=[str(self.id)])