from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from channel import views

urlpatterns = [
    url(r'^channel/$', views.ChannelList().routing),
    url(r'^channel/(?P<pk>[0-9]+)/$', views.ChannelDetail().routing),

    url(r'^group/$', views.GroupList().routing),
    url(r'^group/(?P<pk>[0-9]+)/$', views.GroupDetail().routing),

    url(r'^profile_group/$', views.ProfileGroupList().routing),
    url(r'^profile_group/(?P<pk>[0-9]+)/$', views.ProfileGroupDetail().routing),

    url(r'^profile/$', views.ProfileList().routing),
    url(r'^profile/(?P<pk>[0-9]+)/$', views.ProfileDetail().routing),
]

urlpatterns = format_suffix_patterns(urlpatterns)
