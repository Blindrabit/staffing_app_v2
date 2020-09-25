from django.urls import path
from .views import AllShiftsViews

urlpatterns =[
    path('all/', AllShiftsViews.as_view(), name='shiftlist')
]

