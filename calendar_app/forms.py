from django import forms
from django.forms import ModelForm, DateInput
from calendar_app.models import Event
from django.contrib.auth.models import User


avilibility_choices = (
    (1, 'Avilible to work'),
    (2, 'Busy'),
    (3, 'Booked'),
    (4, 'On Holiday'),
)


class EventForm(ModelForm):
  class Meta:
    model = Event
    avilibility = forms.ChoiceField(required=True, widget=forms.CheckboxInput, choices=avilibility_choices)
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }
    fields = ['avilibility','start_time','end_time']

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats parses HTML5 datetime-local input to datetime field
    self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
    self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)


  def clean(self):
    form_start_time = self.cleaned_data.get('start_time')
    form_end_time = self.cleaned_data.get('end_time')
    between = Event.objects.filter(manage_id=self.instance.manage_id, end_time__gte=form_start_time, start_time__lte=form_end_time)
    if between:
      raise forms.ValidationError('Already Calendar entry for this time')
    super().clean()