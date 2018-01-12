from __future__ import unicode_literals
import time
from django.db import models

class Agent(models.Model):
    name = models.CharField(unique=True, max_length=45, blank=True, null=True)
    ip = models.CharField(unique=True, max_length=45, blank=True, null=True)
    descr = models.CharField(max_length=100, blank=True, null=True, default='')
    thread = models.IntegerField(blank=True, null=True, default=10)
    cpu = models.IntegerField(blank=True, null=True, default=0)
    mem = models.IntegerField(blank=True, null=True, default=0)
    disk = models.IntegerField(blank=True, null=True, default=0)
    last_update = models.IntegerField(blank=True, null=True, default=int(time.time()))
    active = models.IntegerField(blank=True, null=True, default=0)
    lng = models.CharField(max_length=20, blank=True, null=True, default='')
    lat = models.CharField(max_length=20, blank=True, null=True, default='')

    class Meta:
        managed = True
        db_table = 'agent'

    def convert_agent_list_to_single_dictionary(self, agent):
        agrs = {
                    "id"            : int(agent.id),
                    "name"          : agent.name,
                    "ip"            : agent.ip,
                    "descr"         : agent.descr,
                    "thread"        : int(agent.thread),
                    "cpu"           : int(agent.cpu),
                    "mem"           : int(agent.mem),
                    "disk"          : int(agent.disk),
                    "last_update"   : int(agent.last_update),
                    "active"        : int(agent.active),
                    "lng"           : agent.lng,
                    "lat"           : agent.lat
                }
        return agrs


class ProfileAgent(models.Model):
    profile_id = models.IntegerField(blank=True, null=True)
    agent_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True, default=0)
    analyzer_status = models.IntegerField(blank=True, null=True, default=0)
    dropframe = models.IntegerField(blank=True, null=True, default=0)
    dropframe_threshold = models.IntegerField(blank=True, null=True, default=0)
    discontinuity = models.IntegerField(blank=True, null=True, default=0)
    discontinuity_threshold = models.IntegerField(blank=True, null=True, default=0)
    check = models.IntegerField(blank=True, null=True, default=0)
    video = models.IntegerField(blank=True, null=True, default=0)
    audio = models.IntegerField(blank=True, null=True, default=0)
    monitor = models.IntegerField(blank=True, null=True, default=0)
    analyzer = models.IntegerField(blank=True, null=True, default=0)
    last_update = models.IntegerField(blank=True, null=True, default=int(time.time()))

    class Meta:
        managed = True
        db_table = 'profile_agent'
#        unique_together = (('profile_id', 'agent_id'),)
    def convert_profile_agent_list_to_single_dictionary(self, profile_agent):
        agrs = {
                    'id'                        : int(profile_agent.id),
                    'profile_id'                : int(profile_agent.profile_id),
                    'agent_id'                  : int(profile_agent.agent_id),
                    'status'                    : int(profile_agent.status),
                    'analyzer_status'           : int(profile_agent.analyzer_status),
                    'dropframe'                 : int(profile_agent.dropframe),
                    'dropframe_threshold'       : int(profile_agent.dropframe_threshold),
                    'discontinuity'             : int(profile_agent.discontinuity),
                    'discontinuity_threshold'   : int(profile_agent.discontinuity_threshold),
                    'check'                     : int(profile_agent.check),
                    'video'                     : int(profile_agent.video),
                    'audio'                     : int(profile_agent.audio),
                    'monitor'                   : int(profile_agent.monitor),
                    'analyzer'                  : int(profile_agent.analyzer),
                    'last_update'               : int(profile_agent.last_update)
                }
        return agrs

class Server(models.Model):
    name = models.CharField(unique=True, max_length=45, blank=True, null=True)
    ip = models.CharField(unique=True, max_length=45, blank=True, null=True)
    descr = models.CharField(max_length=100, blank=True, null=True, default='')
    os = models.CharField(max_length=32, blank=True, null=True, default='CentOS')
    cpu = models.IntegerField(blank=True, null=True, default=0)
    mem = models.IntegerField(blank=True, null=True, default=0)
    disk = models.IntegerField(blank=True, null=True, default=0)
    last_update = models.IntegerField(blank=True, null=True, default=int(time.time()))
    active = models.IntegerField(blank=True, null=True, default=0)

    class Meta:
        managed = True
        db_table = 'server'