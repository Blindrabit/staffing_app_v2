from django.forms.models import model_to_dict
from datetime import datetime
from django.conf import settings 

from .models import Shifts
from calendar_app.models import Event
from users.models import CustomUser

def autoshiftandeventmatching():
    actual_hos_list = []
    shifts_needing_fill = Shifts.objects.filter(start_time__gte=datetime.now()).filter(manage=None)
    for shift in shifts_needing_fill:
        shift_dict = model_to_dict(shift)
        staff_available = Event.objects.filter(start_time__gte=datetime.now()).filter(availability='Available')
        for event in staff_available:
            event_dict = model_to_dict(event)
            staff_hospital_list = CustomUser.objects.filter(pk=event_dict['manage']).values_list('hospitals')
            for hos in staff_hospital_list:
                actual_hos_list.append(hos[0])
            if (shift_dict['start_time'] >= event_dict['start_time'] and 
                shift_dict['end_time'] <= event_dict['end_time'] and
                shift_dict['hospital'] in actual_hos_list
                ):
                Shifts.objects.filter(pk=shift_dict['id']).update(manage=event_dict['manage'])
                event.availability = "Busy"
                event.save()
                break