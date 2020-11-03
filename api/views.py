from rest_framework import generics, permissions
from shifts.models import Shifts
from .serializers import ShiftSerializer

class ShiftsAPI(generics.ListAPIView):
    queryset = Shifts.objects.all()
    serializer_class = ShiftSerializer

class ShiftDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shifts.objects.all()
    serializer_class = ShiftSerializer
