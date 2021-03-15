from django.urls import path

from .views import AllShiftsViews, CreateShiftView

urlpatterns =[
    path('all/', AllShiftsViews.as_view(), name='shiftlist'),
    path('create/', CreateShiftView.as_view(), name='createshift'),
]

