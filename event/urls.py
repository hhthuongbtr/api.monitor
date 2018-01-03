from django.conf.urls import url
from event import views

urlpatterns = [

    url(r'^$', views.EventList().routing),
    url(r'^standby/$', views.EventList().standby),
    url(r'^(?P<pk>[0-9]+)/$', views.EventDetail().routing),
    url(r'^encoder/$', views.EncoderList().routing),
    url(r'^encoder/standby/$', views.EncoderList().standby),
    url(r'^encoder/(?P<pk>[0-9]+)/$', views.EncoderDetail().routing),
    url(r'^service/$', views.ServiceCheckList().routing),
    url(r'^service/standby/$', views.ServiceCheckList().standby),
    url(r'^service/(?P<pk>[0-9]+)/$', views.ServiceCheckDetail().routing),
    url(r'^event_monitor/$', views.EventMonitorList().routing),
    url(r'^event_monitor/(?P<pk>[0-9]+)/$', views.EventMonitorDetail().routing),
    url(r'^monitor/$', views.MonitorList().routing),
    url(r'^running/$', views.MonitorList().get_running_monitor_list),
    url(r'^waiting/$', views.MonitorList().get_waiting_monitor_list),
    url(r'^completed/$', views.MonitorList().get_completed_monitor_list),
    url(r'^monitor/(?P<event_monitor_id>[0-9]+)/$', views.MonitorDetail().routing),
]

