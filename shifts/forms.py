from django import forms
from django.forms import DateInput

from .models import Shifts

class ShiftForm(forms.ModelForm):
    class Meta:
        model = Shifts
        widgets = {
            'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%d-%m-%Y%H:%M'),
            'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%d-%m-%Y%H:%M'),
            }
        fields= ['hospital', 'area', 'start_time', 'end_time']

    def clean(self, *args, **kwargs):
        form_start_time = self.cleaned_data.get('start_time')
        form_end_time = self.cleaned_data.get('end_time')
        if form_start_time > form_end_time:
            raise forms.ValidationError('End Time must be greater than the Start Time')
        return super().clean()