from django.urls import path
from .views import ShiftsAPI

urlpatterns = [
    path('shifts/', ShiftsAPI.as_view(), name='API-shiftlist'),
]