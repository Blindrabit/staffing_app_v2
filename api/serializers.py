from rest_framework import serializers

from calendar_app.models import Event
from shifts.models import Shifts
from users.models import HospitalListModel, AreaToWorkModel

class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'start_time', 'end_time', 'hospital', 'manage', 'area',)
        model = Shifts

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'start_time', 'end_time', 'availability', 'manage',)
        model = Event

class HosSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'hospital',)
        model = HospitalListModel

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'area')
        model = AreaToWorkModel