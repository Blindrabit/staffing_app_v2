from rest_framework import generics, permissions

from calendar_app.models import Event
from shifts.models import Shifts
from users.models import AreaToWorkModel, HospitalListModel

from .permissions import IsSuperUserOrReadOnly
from .serializers import (AreaSerializer, EventSerializer, HosSerializer,
                          ShiftSerializer)


#Shifts API views
class ShiftsAPI(generics.ListAPIView):
    queryset = Shifts.objects.all()
    serializer_class = ShiftSerializer

class ShiftDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shifts.objects.all()
    serializer_class = ShiftSerializer

class ShiftCreateAPI(generics.CreateAPIView):
    queryset = Shifts.objects.all()
    serializer_class = ShiftSerializer


#Calendar API Views
class CalendarListAPI(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        user = self.request.user.id
        return Event.objects.filter(manage=user)

class CalendarDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        user = self.request.user.id
        return Event.objects.filter(manage=user)

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