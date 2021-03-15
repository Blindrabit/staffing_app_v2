from django import views as django_views
from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^jsi18n/$', django_views.i18n.JavaScriptCatalog.as_view(), name='jsi18n'),
]