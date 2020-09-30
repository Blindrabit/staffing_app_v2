from django.urls import path
from . import views
from django.conf.urls import url
from django import views as django_views

urlpatterns = [
    url(r'^jsi18n/$', django_views.i18n.JavaScriptCatalog.as_view(), name='jsi18n'),
]