from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from channel import views

urlpatterns = [
    url(r'^channel/$', views.ChannelList.as_view()),
    url(r'^channel/(?P<pk>[0-9]+)/$', views.ChannelDetail.as_view()),

    url(r'^group/$', views.GroupList.as_view()),
    url(r'^group/(?P<pk>[0-9]+)/$', views.GroupDetail.as_view()),

    url(r'^profile_group/$', views.ProfileGroupList.as_view()),
    url(r'^profile_group/(?P<pk>[0-9]+)/$', views.ProfileGroupDetail.as_view()),

    url(r'^profile/$', views.ProfileList.as_view()),
    url(r'^profile/(?P<pk>[0-9]+)/$', views.ProfileDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
