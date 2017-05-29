from rest_framework import serializers
from channel.models import *

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('id', 'name', 'descr', 'group_id', 'active')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')


class ProfileGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileGroup
        fields = ('id', 'profile_id', 'group_id')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'ip', 'descr', 'status', 'type', 'channel', 'protocol', 'monitor', 'last_update', 'active')
