from rest_framework import serializers
from log.models import *

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ('id', 'host', 'facility', 'priority', 'level', 'tag', 'datetime', 'program', 'msg', 'seq', 'counter', 'fo', 'lo')