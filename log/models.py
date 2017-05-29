from __future__ import unicode_literals

from django.db import models


class Log(models.Model):
    id = models.BigAutoField(primary_key=True)
    host = models.CharField(max_length=128, blank=True, null=True)
    facility = models.CharField(max_length=10, blank=True, null=True)
    priority = models.CharField(max_length=10, blank=True, null=True)
    level = models.CharField(max_length=10, blank=True, null=True)
    tag = models.CharField(max_length=10, blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    program = models.CharField(max_length=15, blank=True, null=True)
    msg = models.TextField(blank=True, null=True)
    seq = models.BigIntegerField(blank=True, null=True, default=0)
    counter = models.IntegerField(blank=True, null=True, default=0)
    fo = models.DateTimeField(blank=True, null=True)
    lo = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'logs'
