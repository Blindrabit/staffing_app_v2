from django.urls import path
from .views import ShiftsAPI, ShiftDetailAPI

urlpatterns = [
    #shifts APIs
    path('shifts/', ShiftsAPI.as_view(), name='api-shiftlist'),
    path('shifts/<int:pk>/', ShiftDetailAPI.as_view(), name='api-shiftdetail'),

]