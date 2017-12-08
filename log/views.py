from log.models import *
from django.http import Http404, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from setting.customSQL import *
from setting.rabbitmq_queue import *
import json


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
        args = {}
        try:
            log_list = Log.objects.all().order_by('-datetime')[:100]
        except Exception as e:
            args["detail"] = e
        if log_list:
            args_log_list=[]
            for log in log_list:
                args_log_list.append({ 
                    'id'            : int(log.id),
                    'host'          : log.host,
                    'facility'      : log.facility,
                    'priority'      : log.priority,
                    'level'         : log.level,
                    'tag'           : log.tag,
                    'datetime'      : str(log.datetime),
                    'program'       : log.program,
                    'msg'           : log.msg,
                    'seq'           : log.seq,
                    'counter'       : log.counter,
                    'fo'            : log.fo,
                    'lo'            : log.lo
                    })
            args["detail"] = "OK"
            args["log_list"] = args_log_list
        else:
            args["detail"] = "Empty"
        data = json.dumps(args)
        return HttpResponse(data, content_type='application/json', status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data=request.data
        if len(data)==3 and ('host' and 'tag' and 'msg' in data):
            querry="insert into logs(host,tag,datetime,msg) values('%s','%s', NOW(),'%s');"%(data['host'],data['tag'],data['msg'])
            RabbitMQQueue().push_query(querry)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
class LogDetail(APIView):
    """
    Retrieve, update or delete a Log instance.
    """
    def get_object(self, pk):
        try:
            return Log.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return None

    def get(self, request, pk, format=None):
        args = {}
        log = self.get_object(pk)
        if log:
            args_log = []
            args_log.append({
                'id'            : int(log.id),
                'host'          : log.host,
                'facility'      : log.facility,
                'priority'      : log.priority,
                'level'         : log.level,
                'tag'           : log.tag,
                'datetime'      : str(log.datetime),
                'program'       : log.program,
                'msg'           : log.msg,
                'seq'           : log.seq,
                'counter'       : log.counter,
                'fo'            : log.fo,
                'lo'            : log.lo
                })
            args["detail"] = 'OK'
            args['log'] = args_log
        else:
            args["detail"] = 'Not found.'
        data = json.dumps(args)
        return HttpResponse(data, content_type='application/json', status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        return Response(status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        log = self.get_object(pk)
        log.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)