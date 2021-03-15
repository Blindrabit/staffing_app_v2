from allauth.account.forms import SignupForm
from django import forms
from django.contrib.admin import ModelAdmin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm

from .models import AreaToWorkModel, HospitalListModel


class MyCustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name') 
    last_name = forms.CharField(max_length=30, label='Last Name') 
    dbs_number = forms.CharField(max_length=13, label='DBS Number')
    hospitals = forms.ModelMultipleChoiceField(queryset=HospitalListModel.objects.all(), 
                                            widget=FilteredSelectMultiple('HospitalListModel',False), 
                                            required=False, 
                                            )
    area_to_work = forms.ModelMultipleChoiceField(queryset=AreaToWorkModel.objects.all(), 
                                            widget=FilteredSelectMultiple('AreaToWorkModel',False), 
                                            required=False, 
                                            )

    class Media:
        css = {
            'all': ('/static/admin/css/widgets.css',),
        }
        js = ('/admin/jsi18n',)

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.dbs_number = self.cleaned_data['dbs_number']
        cleaned_hos_data = self.cleaned_data['hospitals'].values_list('pk',flat=True)
        cleaned_area_data = self.cleaned_data['area_to_work'].values_list('pk',flat=True)
        user.save()
        for hos in list(cleaned_hos_data):
            user.hospitals.add(hos)
        for area in list(cleaned_area_data):
            user.area_to_work.add(area)
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