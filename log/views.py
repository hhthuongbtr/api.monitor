from log.models import *
from log.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from setting.customSQL import *
from setting.rabbitmq_queue import *


#######################################################################
#                                                                     #
#-------------------------------AGENT---------------------------------#
#                                                                     #
#######################################################################
class LogList(APIView):
    """
    List all Logs, or create a new Log.
    """
    def get(self, request, format=None):
        log = Log.objects.all().order_by('-datetime')[:100]
        serializer = LogSerializer(log, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data=request.data
        if len(data)==3 and ('host' and 'tag' and 'msg' in data):
            querry="insert into logs(host,tag,datetime,msg) values('%s','%s', NOW(),'%s');"%(data['host'],data['tag'],data['msg'])
            RabbitMQQueue().push_query(querry)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
        #serializer = LogSerializer(data=request.data)
        #print query
        #if serializer.is_valid():
        #    serializer.save()
        #   return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class LogDetail(APIView):
    """
    Retrieve, update or delete a Log instance.
    """
    def get_object(self, pk):
        try:
            return Log.objects.get(pk=pk)
        except Log.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        log = self.get_object(pk)
        serializer = LogSerializer(log)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        return Response(status=status.HTTP_400_BAD_REQUEST)
#        log = self.get_object(pk)
#        serializer = LogSerializer(log, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        log = self.get_object(pk)
        log.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)