from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .forms import ShiftForm
from .models import Shifts


class AllShiftsViews(LoginRequiredMixin, ListView):
    model = Shifts
    template_name = 'shiftlist.html'
    context_object_name = 'shift_list'

    def get_queryset(self):
        return Shifts.objects.filter(manage=None)


class CreateShiftView(LoginRequiredMixin, CreateView):
    model = Shifts
    form_class = ShiftForm
    template_name = 'shiftcreate.html'
    success_url = reverse_lazy('shiftlist')
