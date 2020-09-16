from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.http import Http404


from .models import Event
from .forms import EventForm

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
    
    def form_valid(self, EventForm):
        EventForm.instance.manage = self.request.user
        return super().form_valid(EventForm)

class CalendarEventUpdate(LoginRequiredMixin, UpdateView):
    model= Event
    form_class = EventForm
    template_name='calendar_update_event_form.html'

    def get(self, request, *args, **kwargs):
        try:
            return super(CalendarEventUpdate, self).get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('calendar_list'))