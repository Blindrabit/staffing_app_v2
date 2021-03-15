from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Shifts
from .tasks import autoshiftandeventmatching


@receiver(post_save, sender=Shifts)
def shiftsavedsignalreciever(sender, **kwargs):
    pass #autoshiftandeventmatching()