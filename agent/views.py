import time, json
from agent.models import *
from rest_framework import status
from utils.rabbitmq_queue import *
from rest_framework.response import Response
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from scc.views import Scc
from utils.check_iptv import Snmp
from utils.DateTime import DateTime
from BLL.agent import ProfileAgent as ProfileAgentBLL
from setting.settings import PUSH_ALARM as is_push_alarm


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
    def get(self, request):
        args = {}
        try:
            agent_list = Agent.objects.all()
        except Exception as e:
            args["message"] = e
        if agent_list:
            args_agent = []
            for agent in agent_list:
                args_agent.append(Agent().convert_agent_list_to_single_dictionary(agent))
            args["message"] = "OK"
            args["data"] = args_agent
        else:
            args["message"] = "Empty"
        data = json.dumps(args)
        return HttpResponse(data, content_type='application/json', status=202)
        
    @csrf_exempt
    def post(self, request):
        return HttpResponse(status=400)

class AgentDetail:
    """
    Retrieve, update or delete a agent instance.
    """
    @csrf_exempt
    def routing(self, request, ip):
        if request.method == "GET":
            return self.get(request, ip)
        elif request.method == "PUT":
            return self.put(request, ip)
        elif request.method == "DELETE":
            return self.delete(request, ip)

    @csrf_exempt
    def get_object(self, ip):
        try:
            agent = Agent.objects.get(ip=ip)
        except ObjectDoesNotExist:
            agent = None
        return agent

    @csrf_exempt
    def get(self, request, ip):
        args = {}
        agent = self.get_object(ip)
        if agent:
            args_agent = Agent().convert_agent_list_to_single_dictionary(agent)
            args["message"] = 'OK'
            args['data'] = args_agent
        else:
            args["message"] = 'Not found.'
        data = json.dumps(args)
        return HttpResponse(data, content_type='application/json', status=202)

    @csrf_exempt
    def put(self, request, ip):
        data = request.body
        data = json.loads(data)
        if len(data)==3 and('cpu' and 'mem' and 'disk' in data):
            querry = "update agent set cpu=%s,mem=%s,disk=%s,last_update=unix_timestamp() where ip='%s';"%(data['cpu'],data['mem'],data['disk'],ip)
            RabbitMQQueue().push_query(querry)
            return HttpResponse(status=202)
        return HttpResponse(status=400)

    @csrf_exempt
    def delete(self, request, ip):
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

    @csrf_exempt
    def get(self, request):
        args = {}
        try:
            profile_agent_list = ProfileAgent.objects.all()
        except Exception as e:
            args["message"] = e
        if profile_agent_list:
            args_profile_agent = []
            for profile_agent in profile_agent_list:
                args_profile_agent.append(ProfileAgent().convert_profile_agent_list_to_single_dictionary(profile_agent))
            args["message"] = "OK"
            args["data"] = args_profile_agent
        else:
            args["message"] = "Empty"
        data = json.dumps(args)
        return HttpResponse(data, content_type='application/json', status=202)

    @csrf_exempt
    def post(self, request):
        return HttpResponse(status=400)

    #Agent.py get list profile agent by ip
    @csrf_exempt
    def get_profile_agent_monitor_list(self, request, ip):
        pa = ProfileAgentBLL()
        data = pa.get_profile_agent_monitor_list(ip)
        json_data = json.dumps({"data": data['data'], "message": data['message'], "status": 200})
        return HttpResponse(json_data, content_type='application/json', status=200)

    @csrf_exempt
    def get_profile_agent_snmp_list(self, request, ip):
        pa = ProfileAgentBLL()
        data = pa.get_profile_agent_snmp_list(ip)
        json_data = json.dumps({"data": data['data'], "message": data['message'], "status": 200})
        return HttpResponse(json_data, content_type='application/json', status=200)

    @csrf_exempt
    def get_profile_agent_check_video_list(self, request, ip):
        pa = ProfileAgentBLL()
        data = pa.get_profile_agent_check_video_list(ip)
        json_data = json.dumps({"data": data['data'], "message": data['message'], "status": 200})
        return HttpResponse(json_data, content_type='application/json', status=200)

    @csrf_exempt
    def get_profile_agent_first_check_anylazer_list(self, request):
        pa = ProfileAgentBLL()
        data = pa.get_profile_agent_first_check_anylazer_list()
        json_data = json.dumps({"data": data['data'], "message": data['message'], "status": 200})
        return HttpResponse(json_data, content_type='application/json', status=200)

    @csrf_exempt
    def get_profile_agent_last_check_analyzer_list(self, request):
        pa = ProfileAgentBLL()
        data = pa.get_profile_agent_last_check_analyzer_list()
        json_data = json.dumps({"data": data['data'], "message": data['message'], "status": 200})
        return HttpResponse(json_data, content_type='application/json', status=200)


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
    def get(self, request, pk):
        args = {}
        profile_agent = self.get_object(pk)
        if profile_agent:
            args_profile_agent = ProfileAgent().convert_profile_agent_list_to_single_dictionary(profile_agent)
            args["message"] = 'OK'
            args['data'] = args_profile_agent
        else:
            args["message"] = 'Not found.'
        data = json.dumps(args)
        return HttpResponse(data, content_type='application/json', status=202)

    @csrf_exempt
    def put(self, request, pk):
        data = request.body
        data = json.loads(data)
        #Status
        if ("status" in data):
            agent_name = data["agent"]
            if "Origin" in agent_name or "4500" in agent_name:
                profile_agent = self.get_object(pk)
                date_time = DateTime()
                if not profile_agent:
                    return HttpResponse(status=400)
                profile_agent.status = data["status"]
                profile_agent.last_update = date_time.get_now()
                profile_agent.save()
                if is_push_alarm:
                    time.sleep(0.5)
                    snmp = Snmp(str(data["ip"]).replace(' ', ''))
                    alarm_status, msg = snmp.check_agent()
                    data = {
                        "ishost"            : False,
                        "queueServiceName"  : "Check_Agent_IPTV_Status",
                        "queueHost"         : agent_name, 
                        "msg"               : msg,
                        "AlertStatus"       : alarm_status
                    }
                    scc = Scc()
                    scc.post(data)
                return HttpResponse(status=202)
            else:
                querry = "update profile_agent set status=%s,last_update=unix_timestamp() where id=%s;"%(data['status'],pk)
                RabbitMQQueue().push_query(querry)
                return HttpResponse(status=202)
        #video
        elif ('video' in data):
            agent_name = data["agent"]
            if "Origin" in agent_name or "4500" in agent_name:
                profile_agent = self.get_object(pk)
                date_time = DateTime()
                if not profile_agent:
                    return HttpResponse(status=400)
                profile_agent.video = data["video"]
                profile_agent.last_update = date_time.get_now()
                profile_agent.save()
                """
                Push to SCC
                """
                # if is_push_alarm:
                #     time.sleep(0.5)
                #     snmp = Snmp(str(data["ip"]).replace(' ', ''))
                #     alarm_status, msg = snmp.check_agent()
                #     data = {
                #         "ishost"            : False,
                #         "queueServiceName"  : "Check_Agent_IPTV_Status",
                #         "queueHost"         : agent_name, 
                #         "msg"               : msg,
                #         "AlertStatus"       : alarm_status
                #     }
                #     scc = Scc()
                #     scc.post(data)
                return HttpResponse(status=202)
            else:
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
        return HttpResponse(status=400)

    @csrf_exempt
    def delete(self, request, pk):
        profileAgent = self.get_object(pk)
        profileAgent.delete()
        return HttpResponse(status=204)

