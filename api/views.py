from rest_framework import generics, permissions

from shifts.models import Shifts
from calendar_app.models import Event
from users.models import HospitalListModel, AreaToWorkModel

from .serializers import ShiftSerializer, EventSerializer, HosSerializer, AreaSerializer
from .permissions import IsSuperUserOrReadOnly

#Shifts API views
class ShiftsAPI(generics.ListAPIView):
    queryset = Shifts.objects.all()
    serializer_class = ShiftSerializer

class ShiftDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shifts.objects.all()
    serializer_class = ShiftSerializer

class ShiftCreateAPI(generics.CreateAPIView):
    permission_classes = (IsSuperUserOrReadOnly,)
    queryset = Shifts.objects.all()
    serializer_class = ShiftSerializer

#Calendar API Views
class CalendarListAPI(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class CalendarDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class CalendarCreateAPI(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

#Users API views

class HosDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = HospitalListModel.objects.all()
    serializer_class = HosSerializer

class HosListAPI(generics.ListAPIView):
    queryset = HospitalListModel.objects.all()
    serializer_class = HosSerializer

class HosCreateAPI(generics.CreateAPIView):
    queryset = HospitalListModel.objects.all()
    serializer_class = HosSerializer

class AreaDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = AreaToWorkModel.objects.all()
    serializer_class = AreaSerializer

class AreaListAPI(generics.ListAPIView):
    queryset = AreaToWorkModel.objects.all()
    serializer_class = AreaSerializer

class AreaCreateAPI(generics.CreateAPIView):
    queryset = AreaToWorkModel.objects.all()
    serializer_class = AreaSerializer