from django import forms
from django.forms import DateInput

from .models import Shifts

class ShiftForm(forms.ModelForm):
    class Meta:
        model = Shifts
        widgets = {
            'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            }
        fields= ['hospital', 'start_time', 'end_time']