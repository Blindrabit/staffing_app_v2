from .models import Event
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, FormView

class CalendarEventsView(ListView):
    model = Event
    context_object_name = 'event_list'
    template_name = 'calendar_list.html'

class CalendarEventDetail(DetailView):
    model = Event
    context_object_name = 'event'
    template_name = 'calendar_event_detail.html'

class CalendarEventAdd(CreateView):
    model = Event
    fields = ['avilibility', 'start_time', 'end_time' ]
    template_name = 'calendar_create_event.html'

class CalendarEventAdd(FormView):
    model = Event
    fields = ['avilibility', 'start_time', 'end_time' ]
    template_name = 'calendar_create_event_form.html' 