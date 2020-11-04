from django.urls import path
from .views import ShiftsAPI, ShiftDetailAPI, ShiftCreateAPI, ShiftsUpdateAPI, HosDetailAPI

urlpatterns = [
    #shifts APIs
    path('shifts/', ShiftsAPI.as_view(), name='api-shiftlist'),
    path('shifts/create/', ShiftCreateAPI.as_view(), name='api-shiftlist-create'),
    path('shifts/<int:pk>/', ShiftDetailAPI.as_view()),
    path('shifts/<int:pk>/update/', ShiftsUpdateAPI.as_view(), name='api-shiftupdate'),
    path('hos/<int:pk>/', HosDetailAPI.as_view()),

]