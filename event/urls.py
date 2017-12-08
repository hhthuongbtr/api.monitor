from django.conf.urls import url
from event import views

urlpatterns = [

    url(r'^$', views.EventList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.EventDetail.as_view()),
    url(r'^encoder/$', views.EncoderList.as_view()),
    url(r'^encoder/(?P<pk>[0-9]+)/$', views.EncoderDetail.as_view()),
    url(r'^service_check/$', views.ServiceCheckList.as_view()),
    url(r'^service_check/(?P<pk>[0-9]+)/$', views.ServiceCheckDetail.as_view()),
    url(r'^event_monitor/$', views.EventMonitorList.as_view()),
    url(r'^event_monitor/(?P<pk>[0-9]+)/$', views.EventMonitorDetail.as_view()),
    url(r'^monitor/$', views.MonitorList().get_monitor_list),
    url(r'^running/$', views.MonitorList().get_running_monitor_list),
    url(r'^waiting/$', views.MonitorList().get_waiting_monitor_list),
    url(r'^completed/$', views.MonitorList().get_completed_monitor_list),
    url(r'^monitor/(?P<event_monitor_id>[0-9]+)/$', views.MonitorDetail().get_event_monitor),
]