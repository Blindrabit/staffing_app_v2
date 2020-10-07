from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Shifts
from .utils import autoshiftandeventmatching

@receiver(post_save, sender=Shifts)
def shiftsavedsignalreciever(sender, **kwargs):
    autoshiftandeventmatching()