from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from agent import views
from agent.views import *

urlpatterns = [
    url(r'^agent/$', views.AgentList().routing),
    url(r'^agent/(?P<ip>(([01]?[0-9]?[0-9]|2[0-4][0-9]|2[5][0-5])\.){3}([01]?[0-9]?[0-9]|2[0-4][0-9]|2[5][0-5]))/$', views.AgentDetail().routing),
    url(r'^profile_agent/$', views.ProfileAgentList().routing),
    url(r'^profile_agent/(?P<pk>[0-9]+)/$', views.ProfileAgentDetail().routing),
    url(r'^profile_agent/(?P<ip>(([01]?[0-9]?[0-9]|2[0-4][0-9]|2[5][0-5])\.){3}([01]?[0-9]?[0-9]|2[0-4][0-9]|2[5][0-5]))/$', ProfileAgentList().get_monitor_profile_agent_list),
    url(r'^profile_agent/analyzer/$', ProfileAgentList().get_first_check_anylazer_profile_agent_list),
    url(r'^profile_agent/analyzer_check/$', ProfileAgentList().get_last_check_analyzer_profile_agent_list),
    url(r'^profile_agent/snmp/(?P<ip>(([01]?[0-9]?[0-9]|2[0-4][0-9]|2[5][0-5])\.){3}([01]?[0-9]?[0-9]|2[0-4][0-9]|2[5][0-5]))/$', ProfileAgentList().get_snmp_profile_agent_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)
