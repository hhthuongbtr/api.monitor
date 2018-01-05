from agent.models import *
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
import json
from setting.customSQL import *
from setting.rabbitmq_queue import *
from django.core.exceptions import ObjectDoesNotExist


#######################################################################
#                                                                     #
#-------------------------------AGENT---------------------------------#
#                                                                     #
#######################################################################
class AgentList:
    """
    List all Agents, or create a new agent.
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
            agent_list = Agent.objects.all()
        except Exception as e:
            args["detail"] = e
        if agent_list:
            args_agent=[]
            for agent in agent_list:
                args_agent.append({ 
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
                    })
            args["detail"] = "OK"
            args["agent_list"] = args_agent
        else:
            args["detail"] = "Empty"
        data = json.dumps(args)
        return HttpResponse(data, content_type='application/json', status=202)
        
    @csrf_exempt
    def post(self, request, format=None):
        return HttpResponse(status=400)

class AgentDetail:
    """
    Retrieve, update or delete a agent instance.
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
    def get_object(self, ip):
        try:
            agent = Agent.objects.get(ip=ip)
        except ObjectDoesNotExist:
            agent = None
        return agent

    @csrf_exempt
    def get(self, request, ip, format=None):
        args = {}
        agent = self.get_object(ip)
        if agent:
            args_agent = []
            args_agent.append({
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
                })
            args["detail"] = 'OK'
            args['agent'] = args_agent
        else:
            args["detail"] = 'Not found.'
        data = json.dumps(args)
        return HttpResponse(data, content_type='application/json', status=202)

    @csrf_exempt
    def put(self, request, ip, format=None):
        data = request.data
        if len(data)==3 and('cpu' and 'mem' and 'disk' in data):
            querry = "update agent set cpu=%s,mem=%s,disk=%s,last_update=unix_timestamp() where ip='%s';"%(data['cpu'],data['mem'],data['disk'],ip)
            RabbitMQQueue().push_query(querry)
            return HttpResponse(status=202)
        return HttpResponse(status=400)

    @csrf_exempt
    def delete(self, request, ip, format=None):
        return HttpResponse(status=400)

#######################################################################
#                                                                     #
#---------------------------PROFILE AGENT-----------------------------#
#                                                                     #
#######################################################################

class ProfileAgentList:
    """
    List all profile_agents, or create a new profilie_agent.
    """
    @csrf_exempt
    def routing(self, request):
        if request.method == "GET":
            return self.get(request)
        elif request.method == "POST":
            return self.post(request)

    def get(self, request, format=None):
        args = {}
        try:
            profile_agent_list = ProfileAgent.objects.all()
        except Exception as e:
            args["detail"] = e
        if profile_agent_list:
            args_profile_agent=[]
            for profile_agent in profile_agent_list:
                args_profile_agent.append({ 
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
                    })
            args["detail"] = "OK"
            args["profile_agent_list"] = args_profile_agent
        else:
            args["detail"] = "Empty"
        data = json.dumps(args)
        return HttpResponse(data, content_type='application/json', status=202)

    def post(self, request, format=None):
        return Response(serializer.errors, status=400)

class ProfileAgentDetail:
    """
    Retrieve, update or delete a profile_agent instance.
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
            profile_agent = ProfileAgent.objects.get(id = pk)
        except ObjectDoesNotExist:
            profile_agent = None
        return profile_agent

    @csrf_exempt
    def get(self, request, pk, format=None):
        args = {}
        profile_agent = self.get_object(pk)
        if profile_agent:
            args_profile_agent = []
            args_profile_agent.append({
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
                })
            args["detail"] = 'OK'
            args['profile_agent'] = args_profile_agent
        else:
            args["detail"] = 'Not found.'
        data = json.dumps(args)
        return HttpResponse(data, content_type='application/json', status=202)

    @csrf_exempt
    def put(self, request, pk, format=None):
        data=request.data
        #Status
        if ('status' in data) and len(data)==1:
            querry="update profile_agent set status=%s,last_update=unix_timestamp() where id=%s;"%(data['status'],pk)
            RabbitMQQueue().push_query(querry)
            return HttpResponse(status=202)
        #video
        elif ('video' in data) and len(data)==1:
            querry="update profile_agent set video=%s,last_update=unix_timestamp() where id=%s;"%(data['video'],pk)
            RabbitMQQueue().push_query(querry)
            return HttpResponse(status=202)
        #dropframe
        elif ('dropframe' in data) and len(data)==1:
            querry="update profile_agent set dropframe=%s,last_update=unix_timestamp() where id=%s;"%(data['dropframe'],pk)
            RabbitMQQueue().push_query(querry)
            return HttpResponse(status=202)
        #discontinuity
        elif ('discontinuity' in data) and len(data)==1:
            querry="update profile_agent set discontinuity=%s,last_update=unix_timestamp() where id=%s;"%(data['discontinuity'],pk)
            RabbitMQQueue().push_query(querry)
            return HttpResponse(status=202)
        #analyzer_status
        elif ('analyzer_status' in data) and len(data)==1:
            querry="update profile_agent set analyzer_status=%s,last_update=unix_timestamp() where id=%s;"%(data['analyzer_status'],pk)
            RabbitMQQueue().push_query(querry)
            return HttpResponse(status=202)
        return Response(status=400)

    @csrf_exempt
    def delete(self, request, pk, format=None):
        profileAgent = self.get_object(pk)
        profileAgent.delete()
        return Response(status=204)

#Agent.py get list profile agent by ip
def get_profile_agent_by_agent_ip(request, ip):
    cmd="select pa.id,p.ip,p.protocol,pa.status,a.thread,c.name,p.type from profile as p, agent as a, profile_agent as pa,channel as c where a.ip='%s' and a.active=1 and pa.monitor=1 and p.channel_id=c.id and pa.profile_id=p.id and pa.agent_id=a.id"%(ip)
    profile_agent_list = my_custom_sql(cmd)
    if len(profile_agent_list) <1:
        args = []
        args["detail"] = 'Not found.'
        data = json.dumps(args)
        return HttpResponse(data, content_type='application/json', status=204)
    args = []
    for i in profile_agent_list:
        args.append({ 'id'          : i[0] if i[0] else None,
                    'ip'            : i[1] if i[1] else "",
                    'protocol'      : i[2] if i[2] else 'udp',
                    'status'        : i[3] if i[3] else 0,
                    'thread'        : i[4] if i[4] else 10,
                    'name'          : i[5] if i[5] else None,
                    'type'          : i[6] if i[6] else None
                    })
    json_data = json.dumps({"agent": args})
    return HttpResponse(json_data, content_type='application/json', status=200)

def get_profile_agent_analyzer(request):
    cmd="select pa.id,p.ip,a.ip,dropframe,discontinuity from profile_agent as pa, profile as p, agent as a where pa.analyzer=1 and a.active=1 and pa.profile_id=p.id and pa.agent_id=a.id"
    profile_agent_list = my_custom_sql(cmd)
    if len(profile_agent_list) <1:
        args = []
        args["detail"] = 'Not found.'
        data = json.dumps(args)
        return HttpResponse(data, content_type='application/json', status=204)
    args = []
    for i in profile_agent_list:
        args.append({ 'id'          : i[0] if i[0] else None,
                    'ip'            : i[1] if i[1] else "",
                    'agent_ip'      : i[2] if i[2] else "",
                    'dropframe'     : i[3] if i[3] else 0,
                    'discontinuity' : i[4] if i[4] else 0
                    })
    json_data = json.dumps({"profile_analyzer": args})
    return HttpResponse(json_data, content_type='application/json', status=200)

def get_profile_agent_analyzer_check(request):
    cmd="select pa.id,p.ip,a.ip,pa.analyzer_status,pa.dropframe,pa.dropframe_threshold,pa.discontinuity,pa.discontinuity_threshold from profile_agent as pa, profile as p, agent as a where (pa.dropframe > 0 or pa.discontinuity > 0 or analyzer_status !=1) and a.active=1 and pa.analyzer=1 and pa.profile_id=p.id and pa.agent_id=a.id"
    profile_agent_list = my_custom_sql(cmd)
    if len(profile_agent_list) <1:
        args = []
        args["detail"] = 'Not found.'
        data = json.dumps(args)
        return HttpResponse(data, content_type='application/json', status=204)
    args = []
    for i in profile_agent_list:
        args.append({ 'id'                   : i[0] if i[0] else None,
                    'ip'                     : i[1] if i[1] else "",
                    'agent_ip'               : i[2] if i[2] else "",
                    'analyzer_status'        : i[3] if i[3] else 0,
                    'dropframe'              : i[4] if i[4] else 0,
                    'dropframe_threshold'    : i[5] if i[5] else 0,
                    'discontinuity'          : i[6] if i[6] else 0,
                    'discontinuity_threshold': i[7] if i[7] else 0,
                    })
    json_data = json.dumps({"profile_analyzer_check": args})
    return HttpResponse(json_data, content_type='application/json', status=200)

def get_snmp_agent(request,ip):
    cmd="select pa.id,c.name,p.ip,p.type,pa.monitor,pa.status,pa.analyzer,pa.analyzer_status from profile as p, agent as a, profile_agent as pa,channel as c where a.ip='%s' and (pa.monitor=1 or pa.analyzer=1) and a.active=1 and p.channel_id=c.id and pa.profile_id=p.id and pa.agent_id=a.id order by c.name"%(ip)
    profile_agent_list = my_custom_sql(cmd)
    if len(profile_agent_list) <1:
        args = []
        args["detail"] = 'Not found.'
        data = json.dumps(args)
        return HttpResponse(data, content_type='application/json', status=204)
    args = []
    for i in profile_agent_list:
        args.append({ 'id'                   : i[0] if i[0] else None,
                    'name'                   : i[1] if i[1] else "",
                    'ip'                     : i[2] if i[2] else "",
                    'type'                   : i[3] if i[3] else "",
                    'monitor'                : i[4] if i[4] else 0,
                    'status'                 : i[5] if i[5] else 0,
                    'analyzer'               : i[6] if i[6] else 0,
                    'analyzer_status'        : i[7] if i[7] else 0,
                    })
    json_data = json.dumps({"profile_agent_snmp": args})
    return HttpResponse(json_data, content_type='application/json', status=200)
