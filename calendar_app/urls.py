from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

from .views import CalendarEventsView, CalendarEventDetail, CalendarEventAdd


urlpatterns = [
    path('', CalendarEventsView.as_view(), name='calendar_list'),
    path('<uuid:pk>/', CalendarEventDetail.as_view(), name='calendar_event_detail'),
    path('create/', CalendarEventAdd.as_view(), name='Event_add' )
]