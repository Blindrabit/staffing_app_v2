from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import HospitalListModel, AreaToWorkModel
from .forms import CustomUserChangeForm

CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'dbs_number']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(HospitalListModel)
admin.site.register(AreaToWorkModel)