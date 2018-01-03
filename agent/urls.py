from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from agent import views
from agent.views import *

urlpatterns = [
    url(r'^agent/$', views.AgentList().routing),
    url(r'^agent/(?P<ip>(([01]?[0-9]?[0-9]|2[0-4][0-9]|2[5][0-5])\.){3}([01]?[0-9]?[0-9]|2[0-4][0-9]|2[5][0-5]))/$', views.AgentDetail().routing),
    url(r'^profile_agent/$', views.ProfileAgentList().routing),
    url(r'^profile_agent/(?P<pk>[0-9]+)/$', views.ProfileAgentDetail().routing),
    url(r'^profile_agent/(?P<ip>(([01]?[0-9]?[0-9]|2[0-4][0-9]|2[5][0-5])\.){3}([01]?[0-9]?[0-9]|2[0-4][0-9]|2[5][0-5]))/$', get_profile_agent_by_agent_ip),
    url(r'^profile_agent/analyzer/$', get_profile_agent_analyzer),
    url(r'^profile_agent/analyzer_check/$', get_profile_agent_analyzer_check),
    url(r'^profile_agent/snmp/(?P<ip>(([01]?[0-9]?[0-9]|2[0-4][0-9]|2[5][0-5])\.){3}([01]?[0-9]?[0-9]|2[0-4][0-9]|2[5][0-5]))/$', get_snmp_agent),
]

urlpatterns = format_suffix_patterns(urlpatterns)
