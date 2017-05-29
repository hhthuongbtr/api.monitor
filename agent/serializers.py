from rest_framework import serializers
from agent.models import *

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ('id', 'name', 'ip', 'descr', 'thread', 'cpu', 'mem', 'disk', 'last_update', 'active', 'lng', 'lat')

class ProfileAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileAgent
        fields = ('id', 'profile_id', 'agent_id', 'status', 'analyzer_status', 'dropframe', 'dropframe_threshold', 'discontinuity', 'discontinuity_threshold', 'check', 'video', 'audio', 'monitor', 'analyzer', 'last_update')
