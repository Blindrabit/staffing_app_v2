from django.urls import path

from .views import *

urlpatterns = [
    #shifts APIs
    path('shifts/', ShiftsAPI.as_view(), name='api-shift-list'),
    path('shifts/create/', ShiftCreateAPI.as_view(), name='api-shift-create'),
    path('shifts/<int:pk>/', ShiftDetailAPI.as_view(), name='api-shift-detail-update'),
    #calendar APIs
    path('calendar/', CalendarListAPI.as_view(), name='api-calendar-list'),
    path('calendar/<uuid:pk>/', CalendarDetailAPI.as_view(), name='api-calendar-detail-update'),
    path('calendar/create/', CalendarCreateAPI.as_view(), name='api-calendar-create'),
    #user APIs
    path('hos/<int:pk>/', HosDetailAPI.as_view(), name='api-hospital-detail-update'),
    path('hos/', HosListAPI.as_view(), name='api-hospital-list'),
    path('hos/create/', HosCreateAPI.as_view(), name='api-hospital-create'),
    path('area/<int:pk>/', AreaDetailAPI.as_view(), name='api-area-detail-update'),
    path('area/', AreaListAPI.as_view(), name='api-area-list'),
    path('area/create/', AreaCreateAPI.as_view(), name='api-area-create'),
]