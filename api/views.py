from rest_framework import generics, permissions

from shifts.models import Shifts
from calendar_app.models import Event
from users.models import HospitalListModel

from .serializers import ShiftSerializer, HosSerializer
from .permissions import IsSuperUserOrReadOnly

class ShiftsAPI(generics.ListAPIView):
    queryset = Shifts.objects.all()
    serializer_class = ShiftSerializer

class ShiftsUpdateAPI(generics.RetrieveUpdateAPIView):
    queryset = Shifts.objects.all()
    serializer_class = ShiftSerializer

class HosDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = HospitalListModel.objects.all()
    serializer_class = HosSerializer


class ShiftDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shifts.objects.all()
    serializer_class = ShiftSerializer

class ShiftCreateAPI(generics.CreateAPIView):
    permission_classes = (IsSuperUserOrReadOnly,)
    queryset = Shifts.objects.all()
    serializer_class = ShiftSerializer