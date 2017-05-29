from __future__ import unicode_literals
import time
from django.db import models


class Channel(models.Model):
    name = models.CharField(max_length=45, blank=True)
    descr = models.CharField(max_length=100, blank=True, null=True, default='')
    group_id = models.IntegerField(blank=True, default=0)
    active = models.IntegerField(blank=True, default=0)

    class Meta:
        managed = True
        db_table = 'channel'
	ordering = ('name',)

class Group(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = True
        db_table = 'group'


class Profile(models.Model):
    ip = models.CharField(max_length=100, blank=True, null=True)
    descr = models.CharField(max_length=100, blank=True, null=True, default='')
    status = models.IntegerField(blank=True, null=True, default=0)
    type = models.CharField(max_length=32, blank=True, null=True)
    channel = models.ForeignKey(Channel, models.DO_NOTHING, blank=True, null=True)
    protocol = models.CharField(max_length=10, blank=True, null=True, default='udp')
    monitor = models.IntegerField(blank=True, null=True, default=0)
    last_update = models.IntegerField(blank=True, null=True, default=int(time.time()))
    active = models.IntegerField(blank=True, null=True, default=0)

    class Meta:
        managed = True
        db_table = 'profile'


class ProfileGroup(models.Model):
    profile_id = models.IntegerField(blank=True, null=True)
    permission = models.SmallIntegerField(blank=True, null=True, default=0)
    group_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'profile_group'
#	ordering = ('group_id',)
#        unique_together = (('profile_id', 'group_id'),)
