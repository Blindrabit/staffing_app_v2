from rest_framework import serializers

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from dj_rest_auth.registration.serializers import RegisterSerializer

from calendar_app.models import Event
from shifts.models import Shifts
from users.models import HospitalListModel, AreaToWorkModel
from django.contrib.auth import get_user_model



class CustomRegisterSerializer(RegisterSerializer):
    dbs_number = serializers.CharField(max_length=13, required=True)
    hospitals = serializers.PrimaryKeyRelatedField(many=True, queryset=HospitalListModel.objects.all())
    area_to_work = serializers.PrimaryKeyRelatedField(many=True, queryset=AreaToWorkModel.objects.all())

    def get_cleaned_date(self):
        data_dict = super().get_cleaned_data()
        data_dict['dbs_number'] = self.validated_data.get('dbs_number', '')
        data_dict['hospitals'] = self.validated_data.get('hospitals', '')
        data_dict['area_to_work'] = self.validated_data.get('area_to_work', '')
        return data_dict

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

