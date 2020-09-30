from django.forms.models import model_to_dict
from datetime import datetime

from .models import Shifts
from calendar_app.models import Event

def autoshiftandeventmatching(self):

    shifts_needing_fill = Shifts.objects.filter(start_time__gte=datetime.now()).filter(manage=None)
    for shift in shifts_need_filling:
        shift_dict = model_to_dict(shift)
        staff_avilible = Events.objects.filter(start_time__gte=datetime.now()).filter(availability='Available')
        for event in availible_shifts:
            event_dict = model_to_dict(event)
            x
        