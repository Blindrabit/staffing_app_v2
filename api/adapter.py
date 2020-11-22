from allauth.account.adapter import DefaultAccountAdapter

from users.models import HospitalListModel

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        data = form.data
        user.dbs_number = data['dbs_number']
        user.save()
        user.hospitals.add(*data['hospitals'])
        user.area_to_work.add(*data['area_to_work'])
        user.save()
        return user