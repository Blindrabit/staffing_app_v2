from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        data = form.data
        user.dbs_number = data['dbs_number']
        user.save()
        user.hospitals.set(*data['hospitals'])
        user.area_to_work.set(*data['area_to_work'])
        return user