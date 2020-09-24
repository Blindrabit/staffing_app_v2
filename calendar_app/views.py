from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from datetime import datetime, timedelta, date
from django.utils.safestring import mark_safe
import calendar

from .models import Event
from .forms import EventForm
from .utils import Calendar

class CalendarEventsView(LoginRequiredMixin, ListView):
    model = Event
    context_object_name = 'event_list'
    template_name = 'calendar_list.html'
    def get_queryset(self):
        return Event.objects.filter(manage=self.request.user)

class CalendarEventDetail(LoginRequiredMixin, DetailView):
    model = Event
    context_object_name = 'event'
    template_name = 'calendar_event_detail.html'
    def get_queryset(self):
        return Event.objects.filter(manage=self.request.user)

    def get(self, request, *args, **kwargs):
        try:
            return super(CalendarEventDetail, self).get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('calendar_list'))

class CalendarEventAdd(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'calendar_create_event_form.html' 
    success_url = reverse_lazy('calendar_list')

    def form_valid(self, form):
        form.instance.manage = self.request.user
        return super(CalendarEventAdd, self).form_valid(form)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CalendarEventAdd, self).get_form_kwargs()
        kwargs['user_id'] = self.request.user.pk
        return kwargs
    

class CalendarEventUpdate(LoginRequiredMixin, UpdateView):
    model= Event
    form_class = EventForm
    template_name='calendar_update_event_form.html'
    def get_queryset(self):
        return Event.objects.filter(manage=self.request.user)

    def get(self, request, *args, **kwargs):
        try:
            return super(CalendarEventUpdate, self).get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('calendar_list'))

class CalendarView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'calendar.html'
    context_object_name = 'event_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(self.request.user, withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

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