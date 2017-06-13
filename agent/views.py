from agent.models import *
from agent.serializers import *
from django.http import Http404, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json

from setting.customSQL import *
from setting.rabbitmq_queue import *


#######################################################################
#                                                                     #
#-------------------------------AGENT---------------------------------#
#                                                                     #
#######################################################################
class AgentList(APIView):
    """
    List all Agents, or create a new agent.
    """
    def get(self, request, format=None):
        agent = Agent.objects.all()
        serializer = AgentSerializer(agent, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AgentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class AgentDetail(APIView):
    """
    Retrieve, update or delete a agent instance.
    """
    def get_object(self, ip):
        try:
            return Agent.objects.get(ip=ip)
        except Agent.DoesNotExist:
            return HttpResponse({detail: "Not found."}, content_type='application/json', status=status.HTTP_204_NO_CONTENT)

    def get(self, request, ip, format=None):
        agent = self.get_object(ip)
        serializer = AgentSerializer(agent)
        return Response(serializer.data)

    def put(self, request, ip, format=None):
        data = request.data
        if len(data)==3 and('cpu' and 'mem' and 'disk' in data):
            querry = "update agent set cpu=%s,mem=%s,disk=%s,last_update=unix_timestamp() where ip='%s';"%(data['cpu'],data['mem'],data['disk'],ip)
            RabbitMQQueue().push_query(querry)
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, ip, format=None):
        agent = self.get_object(ip)
        agent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#######################################################################
#                                                                     #
#---------------------------PROFILE AGENT-----------------------------#
#                                                                     #
#######################################################################

class ProfileAgentList(APIView):
    """
    List all profile_agents, or create a new profilie_agent.
    """
    def get(self, request, format=None):
        profileAgent = ProfileAgent.objects.all()
        serializer = ProfileAgentSerializer(profileAgent, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfileAgentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ProfileAgentDetail(APIView):
    """
    Retrieve, update or delete a profile_agent instance.
    """
    def get_object(self, pk):
        try:
            return ProfileAgent.objects.get(pk=pk)
        except ProfileAgent.DoesNotExist:
            return HttpResponse({"detail": "Not found."}, content_type='application/json', status=status.HTTP_204_NO_CONTENT)

    def get(self, request, pk, format=None):
        profileAgent = self.get_object(pk)
        serializer = ProfileAgentSerializer(profileAgent)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        data=request.data
        #Status
        if ('status' in data) and len(data)==1:
            querry="update profile_agent set status=%s,last_update=unix_timestamp() where id=%s;"%(data['status'],pk)
            RabbitMQQueue().push_query(querry)
            return Response(status=status.HTTP_202_ACCEPTED)
        #video
        elif ('video' in data) and len(data)==1:
            querry="update profile_agent set video=%s,last_update=unix_timestamp() where id=%s;"%(data['video'],pk)
            RabbitMQQueue().push_query(querry)
            return Response(status=status.HTTP_202_ACCEPTED)
        #dropframe
        elif ('dropframe' in data) and len(data)==1:
            querry="update profile_agent set dropframe=%s,last_update=unix_timestamp() where id=%s;"%(data['dropframe'],pk)
            RabbitMQQueue().push_query(querry)
            return Response(status=status.HTTP_202_ACCEPTED)
        #discontinuity
        elif ('discontinuity' in data) and len(data)==1:
            querry="update profile_agent set discontinuity=%s,last_update=unix_timestamp() where id=%s;"%(data['discontinuity'],pk)
            RabbitMQQueue().push_query(querry)
            return Response(status=status.HTTP_202_ACCEPTED)
        #analyzer_status
        elif ('analyzer_status' in data) and len(data)==1:
            querry="update profile_agent set analyzer_status=%s,last_update=unix_timestamp() where id=%s;"%(data['analyzer_status'],pk)
            RabbitMQQueue().push_query(querry)
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profileAgent = self.get_object(pk)
        profileAgent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Agent.py get list profile agent by ip
def get_profile_agent_by_agent_ip(request, ip):
    cmd="select pa.id,p.ip,p.protocol,pa.status,a.thread,c.name,p.type from profile as p, agent as a, profile_agent as pa,channel as c where a.ip='%s' and a.active=1 and pa.monitor=1 and p.channel_id=c.id and pa.profile_id=p.id and pa.agent_id=a.id"%(ip)
    profile_agent_list = my_custom_sql(cmd)
    if len(profile_agent_list) <1:
        return HttpResponse(json.dumps({"detail": "Not found."}), content_type='application/json', status=status.HTTP_204_NO_CONTENT)
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
        return HttpResponse(json.dumps({"detail": "Not found."}), content_type='application/json', status=status.HTTP_204_NO_CONTENT)
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
    cmd="select pa.id,p.ip,a.ip,pa.analyzer_status,pa.dropframe,pa.dropframe_threshold,pa.discontinuity,pa.discontinuity_threshold from profile_agent as pa, profile as p, agent as a where (pa.dropframe > 0 or pa.discontinuity > 0) and a.active=1 and pa.analyzer=1 and pa.profile_id=p.id and pa.agent_id=a.id"
    profile_agent_list = my_custom_sql(cmd)
    if len(profile_agent_list) <1:
        return HttpResponse({"detail": "Not found."}, content_type='application/json', status=status.HTTP_204_NO_CONTENT)
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
        return HttpResponse({"detail": "Not found."}, content_type='application/json', status=status.HTTP_204_NO_CONTENT)
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
