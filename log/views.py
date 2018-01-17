import json
from log.models import *
from utils.rabbitmq_queue import *
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt


#######################################################################
#                                                                     #
#-------------------------------AGENT---------------------------------#
#                                                                     #
#######################################################################
class LogList:
    """
    List all Logs, or create a new Log.
    """
    @csrf_exempt
    def routing(self, request):
        if request.method == "GET":
            return self.get(request)
        elif request.method == "POST":
            return self.post(request)

    @csrf_exempt
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
        return HttpResponse(data, content_type='application/json', status=200)

    @csrf_exempt
    def post(self, request, format=None):
        data = request.body
        data = json.loads(data)
        if len(data)==3 and ('host' and 'tag' and 'msg' in data):
            querry="insert into logs(host,tag,datetime,msg) values('%s','%s', NOW(),'%s');"%(data['host'],data['tag'],data['msg'])
            RabbitMQQueue().push_query(querry)
            return HttpResponse(status=201)
        return HttpResponse(status=400)

class LogDetail:
    """
    Retrieve, update or delete a Log instance.
    """
    @csrf_exempt
    def routing(self, request, pk):
        if request.method == "GET":
            return self.get(request, pk)
        elif request.method == "PUT":
            return self.put(request, pk)
        elif request.method == "DELETE":
            return self.delete(request, pk)
    @csrf_exempt
    def get_object(self, pk):
        try:
            return Log.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return None
    @csrf_exempt
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

    @csrf_exempt
    def put(self, request, pk, format=None):
        return HttpResponse(status=400)

    @csrf_exempt
    def delete(self, request, pk, format=None):
        log = self.get_object(pk)
        log.delete()
        return HttpResponse(status=204)