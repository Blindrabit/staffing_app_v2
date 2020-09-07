from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required


app_name = 'calendar_app'
urlpatterns = [
    url(r'^calendar/$', login_required(views.CalendarView.as_view()), name='calendar'),
    url(r'^event/new/$', login_required(views.event), name='event_new'),
    url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
]