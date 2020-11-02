from rest_framework import serializers
from shifts.models import Shifts

class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model=Shifts
        fields = ('start_time', 'end_time', 'hospital', 'manage', 'area')
