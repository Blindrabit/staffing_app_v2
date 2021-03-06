from django import forms
from django.forms import DateInput

from .models import Event


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        widgets = {
            'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }
        fields = ['availability', 'start_time', 'end_time']

    def __init__(self, *args, user_id=None, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.user_id = user_id
        # input_formats parses HTML5 datetime-local input to datetime field
        self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)

    def clean(self, *args, **kwargs):
        form_start_time = self.cleaned_data.get('start_time')
        form_end_time = self.cleaned_data.get('end_time')
        form_manage_id = self.cleaned_data.get('manage_id')
        between = Event.objects.exclude(pk=self.instance.pk).filter(
            manage_id=self.user_id,
            end_time__gte=form_start_time,
            start_time__lte=form_end_time
        )
        if between.exists():
            raise forms.ValidationError('Already Calendar entry for this time')
        elif form_start_time > form_end_time:
            raise forms.ValidationError(
                'End Time must be greater than the Start Time')
        return super().clean()
