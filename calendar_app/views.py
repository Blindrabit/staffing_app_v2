from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import *
from .utils import Calendar
from .forms import EventForm
#from shiftDB.tasks import shift_book
import calendar

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect



class CalendarView(generic.ListView):
    model = Event
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        #shift_book()
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(self.request.user, withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        
        return context



def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()



def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id, manage_id=request.get_user_model.pk)
    else:
        instance = Event(manage_id=request.get_user_model.pk)
    
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('calendar_app:calendar')
    else:
        form = EventForm(instance=instance)
    return render(request, 'event.html', {'form': form})