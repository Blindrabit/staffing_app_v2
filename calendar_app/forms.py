from django import forms

aviliblity_choices = (
    (1, 'avilible'),
    (2, 'busy'),
)

class EventForm(forms.Form):

    aviliblity = forms.ChoiceField(choices=aviliblity_choices)
