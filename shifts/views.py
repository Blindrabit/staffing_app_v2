from django.shortcuts import render
from django.views.generic import ListView, TemplateView


class AllShiftsViews(TemplateView):
    template_name = 'shiftlist.html'