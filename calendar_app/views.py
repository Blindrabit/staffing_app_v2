from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Event
from .forms import EventForm

class CalendarEventsView(ListView):
    model = Event
    context_object_name = 'event_list'
    template_name = 'calendar_list.html'

class CalendarEventDetail(DetailView):
    model = Event
    context_object_name = 'event'
    template_name = 'calendar_event_detail.html'

class CalendarEventAdd(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'calendar_create_event_form.html' 
    success_url = reverse_lazy('calendar_list')
    
    def form_valid(self, EventForm):
        EventForm.instance.manage = self.request.user
        return super().form_valid(EventForm)

class CalendarEventUpdate(UpdateView):
    model= Event
    form_class = EventForm
    template_name='calendar_update_event_form.html'