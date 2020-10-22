from __future__ import absolute_import, unicode_literals
from django.forms.models import model_to_dict
from datetime import datetime
from django.conf import settings 
from celery import shared_task

from .models import Shifts
from calendar_app.models import Event 
from users.models import CustomUser, HospitalListModel, AreaToWorkModel

@shared_task
def autoshiftandeventmatching():
    shifts_needing_fill = Shifts.objects.filter(start_time__gte=datetime.now()).filter(manage=None)
    for shift in shifts_needing_fill:
        shift_dict = model_to_dict(shift)
        staff_available = Event.objects.filter(start_time__gte=datetime.now()).filter(availability='Available')
        for event in staff_available:
            event_dict = model_to_dict(event)
            staff_hospital_list = CustomUser.objects.filter(pk=event_dict['manage']).values_list('hospitals')
            staff_area_list = CustomUser.objects.filter(pk=event_dict['manage']).values_list('area_to_work')
            actual_hos_list = []
            actual_area_list = []
            for hos in staff_hospital_list:
                actual_hos_list.append(hos[0])
            for area in staff_area_list:
                actual_area_list.append(area[0])
            hospital = HospitalListModel.objects.get(pk=shift_dict['hospital'])
            hospital_dict = model_to_dict(hospital)
            area = AreaToWorkModel.objects.get(pk=shift_dict['area'])
            area_dict = model_to_dict(area)
            if (shift_dict['start_time'] >= event_dict['start_time'] and 
                shift_dict['end_time'] <= event_dict['end_time'] and
                shift_dict['hospital'] in actual_hos_list and
                shift_dict['area'] in actual_area_list
                ):
                Shifts.objects.filter(pk=shift_dict['id']).update(manage=event_dict['manage'])
                event.availability = "Booked"
                event.start_time = shift_dict['start_time']
                event.end_time = shift_dict['end_time']
                event.hospital = hospital_dict['hospital']
                event.area = area_dict['area']
                event.save()
                break

@shared_task
def add(x,y):
    return x + y