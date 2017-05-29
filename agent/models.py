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