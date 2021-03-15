from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import (CalendarEventAdd, CalendarEventDetail, CalendarEventsView,
                    CalendarEventUpdate, CalendarView)

urlpatterns = [
    path('list/', CalendarEventsView.as_view(), name='calendar_list'),
    path('<uuid:pk>/', CalendarEventDetail.as_view(), name='calendar_event_detail'),
    path('create/', CalendarEventAdd.as_view(), name='event_add' ),
    path('<uuid:pk>/update/', CalendarEventUpdate.as_view(), name='calendar_event_detail_update'),
    path('', CalendarView.as_view(), name='calendar'),
]