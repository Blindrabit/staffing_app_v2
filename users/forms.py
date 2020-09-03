from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm

from allauth.account.forms import SignupForm

class MyCustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name') 
    last_name = forms.CharField(max_length=30, label='Last Name') 
    dbs_number = forms.CharField(max_length=13, label='DBS Number')

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.dbs_number = self.cleaned_data['dbs_number']
        user.save()
        return user

    def signup(self, request, user): 
        user.first_name = self.cleaned_data['first_name'] 
        user.last_name = self.cleaned_data['last_name'] 
        user.save() 
        return user 



class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = get_user_model()
        fields = ('email', 'username','dbs_number')