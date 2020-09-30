import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.conf import settings


class Event(models.Model):

    availability_choices = [
        ('Available', 'Available'),
        ('Busy', 'Busy'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    manage = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    availability = models.CharField(max_length=10, choices=availability_choices, editable=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    

    def __str__(self):
        return self.availability + " - " + str(self.start_time) + " - " + str(self.end_time)

    def get_absolute_url(self):
        return reverse('calendar_event_detail', args=[str(self.id)])

    def get_absolute_url_edit(self):
        return reverse('calendar_event_detail_update', args=[str(self.id)])
    
    def get_html_url(self):
        url = reverse('event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.availability} </a>'