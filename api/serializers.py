from rest_framework import serializers
from shifts.models import Shifts
from users.models import HospitalListModel

class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'start_time', 'end_time', 'hospital', 'manage', 'area',)
        model = Shifts

class HosSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'hospital',)
        model = HospitalListModel