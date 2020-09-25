from django.conf.urls import url
from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import CalendarEventsView, CalendarEventDetail, CalendarEventAdd, CalendarEventUpdate, CalendarView

urlpatterns = [
    path('', CalendarEventsView.as_view(), name='calendar_list'),
    path('<uuid:pk>/', CalendarEventDetail.as_view(), name='calendar_event_detail'),
    path('create/', CalendarEventAdd.as_view(), name='event_add' ),
    path('<uuid:pk>/update/', CalendarEventUpdate.as_view(), name='calendar_event_detail_update'),
    path('calendar/', CalendarView.as_view(), name='calendar'),
]