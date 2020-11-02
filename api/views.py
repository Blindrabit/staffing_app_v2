from rest_framework import generics
from shifts.models import Shifts
from .serializers import ShiftSerializer

class ShiftsAPI(generics.ListAPIView):
    queryset = Shifts.objects.all()
    serializer_class = ShiftSerializer