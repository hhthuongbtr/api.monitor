from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from log import views

urlpatterns = [
    url(r'^log/$', views.LogList.as_view()),
    url(r'^log/(?P<pk>[0-9]+)/$', views.LogDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
