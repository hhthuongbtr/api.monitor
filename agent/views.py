import logging
import time, json
from agent.models import *
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from scc import Scc
from BLL import ProfileAgent as ProfileAgentBLL
from utils import RabbitMQQueue, Snmp, DateTime
from setting.settings import PUSH_ALARM_CORE, PUSH_ALARM_PROBE


#######################################################################
#                                                                     #
#-------------------------------AGENT---------------------------------#
#                                                                     #
#######################################################################
class AgentList:
    """
    List all Agents, or create a new agent.
    """
    def __init__(self):
        self.logger = logging.getLogger("probe")

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
            self.logger.error("status: %d message: %s"%(1, str(e)))
            args["message"] = e
        if agent_list:
            args_agent = []
            for agent in agent_list:
                args_agent.append(Agent().convert_agent_list_to_single_dictionary(agent))
            args["message"] = "OK"
            args["data"] = args_agent
        else:
            args["message"] = "Empty"
            self.logger.warning("status: %d message: %s"%(0, "Empty"))
        data = json.dumps(args)
        return HttpResponse(data, content_type='application/json', status=202)
        
    @csrf_exempt
    def post(self, request):
        return HttpResponse(status=400)

class AgentDetail:
    """
    Retrieve, update or delete a agent instance.
    """
    def __init__(self):
        self.logger = logging.getLogger("probe")

    @csrf_exempt
    def routing(self, request, ip):
        if request.method == "GET":
            return self.get(request, ip)
        elif request.method == "PUT":
            return self.put(request, ip)
        elif request.method == "DELETE":
            return self.delete(request, ip)
        else:
            self.logger.warning("status: %d message: unsuport method %s"%(0, request.method))

    @csrf_exempt
    def get_object(self, ip):
        try:
            agent = Agent.objects.get(ip=ip)
        except ObjectDoesNotExist:
            self.logger.warning("message: profile id %s not exist"%(str(ip)))
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
            self.logger.warning("status: %d message: %s"%(0, "Empty"))
        data = json.dumps(args)
        return HttpResponse(data, content_type='application/json', status=202)

    @csrf_exempt
    def put(self, request, ip):
        self.logger.debug("message: Agent IP :%s"%(str(ip)))
        data = request.body
        data = json.loads(data)
        if len(data)==3 and('cpu' and 'mem' and 'disk' in data):
            querry = "update agent set cpu=%s,mem=%s,disk=%s,last_update=unix_timestamp() where ip='%s';"%(data['cpu'],data['mem'],data['disk'],ip)
            RabbitMQQueue().push_query(querry)
            self.logger.info("message: update performance added to RabbitMQQueue: %s"%(querry))
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
    def __init__(self):
        self.logger = logging.getLogger("probe")

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
            self.logger.error("status: %d message: %s"%(1, str(e)))
            args["message"] = e
        if profile_agent_list:
            args_profile_agent = []
            for profile_agent in profile_agent_list:
                args_profile_agent.append(ProfileAgent().convert_profile_agent_list_to_single_dictionary(profile_agent))
            args["message"] = "OK"
            self.logger.debug("status: %d message: total %d"%(0, len(args_profile_agent)))
            args["data"] = args_profile_agent
        else:
            args["message"] = "Empty"
            self.logger.warning("status: %d message: %s"%(0, "Empty"))
        data = json.dumps(args)
        return HttpResponse(data, content_type='application/json', status=202)

    @csrf_exempt
    def post(self, request):
        self.logger.warning("status: %d Unsupport: %s method"%(0, str(request.method)))
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
    def __init__(self):
        self.logger = logging.getLogger("probe")

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
            self.logger.warning("message: profile id %s not exist"%(str(pk)))
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
            self.logger.warning("message: profile id %s not exist"%(str(pk)))
            args["message"] = 'Not found.'
        data = json.dumps(args)
        return HttpResponse(data, content_type='application/json', status=202)

    @csrf_exempt
    def put(self, request, pk):
        data = request.body
        data = json.loads(data)
        self.logger.debug("message: %s"%(str(data)))
        #Status
        if ("status" in data):
            self.logger.debug("message: update status -->%s"%(str(data)))
            agent_name = data["agent"]
            profile_agent = self.get_object(pk)
            date_time = DateTime()
            if not profile_agent:
                return HttpResponse(status=400)
            if profile_agent.status != data["status"]
                profile_agent.status = data["status"]
                profile_agent.last_update = date_time.get_now()
                profile_agent.save()
                self.logger.debug("message: update status --> success")
                if "Origin" in agent_name or "4500" in agent_name or "ott" in agent_name:
                    self.logger.info("%s is core probe"%(agent_name))
                    if PUSH_ALARM_CORE:
                        self.logger.info("Push alarm to scc is active")
                        time.sleep(0.5)
                        snmp = Snmp(str(data["ip"]).replace(' ', ''))
                        alarm_status, msg = snmp.check_agent()
                        data = {
                            "ishost"            : False,
                            "queueServiceName"  : "Check_Agent_IPTV_Status",
                            "queueHost"         : agent_name, 
                            "msg"               : str(msg),
                            "AlertStatus"       : alarm_status
                        }
                        self.logger.debug("alarm contain: %s"%(str(data)))
                        scc = Scc()
                        scc.post(data)
                    return HttpResponse(status=202)
                else:
                    self.logger.info("%s is not core probe"%(agent_name))
                    if PUSH_ALARM_PROBE:
                        self.logger.info("Push alarm to scc is active")
                        time.sleep(0.5)
                        snmp = Snmp(str(data["ip"]).replace(' ', ''))
                        alarm_status, msg = snmp.check_agent()
                        data = {
                            "ishost"            : False,
                            "queueServiceName"  : "Check_Agent_IPTV_Status",
                            "queueHost"         : agent_name, 
                            "msg"               : str(msg),
                            "AlertStatus"       : alarm_status
                        }
                        self.logger.debug("alarm contain: %s"%(str(data)))
                        scc = Scc()
                        scc.post(data)
                    return HttpResponse(status=202)
            else:
                self.logger.warning("Value not change: %s"%(str(pk)))
                return HttpResponse(status=400)
                # querry = "update profile_agent set status=%s,last_update=unix_timestamp() where id=%s;"%(data['status'],pk)
                # RabbitMQQueue().push_query(querry)
                # return HttpResponse(status=202)
        #video
        elif ('video' in data):
            self.logger.debug("message: update video status -->%s"%(str(data)))
            agent_name = data["agent"]
            profile_agent = self.get_object(pk)
            date_time = DateTime()
            if not profile_agent:
                self.logger.warning("message: profile id %s not exist"%(str(pk)))
                return HttpResponse(status=400)
            if profile_agent.video != data["video"]
                profile_agent.video = data["video"]
                profile_agent.last_update = date_time.get_now()
                profile_agent.save()
                self.logger.debug("message: update video status --> success")
                if "Origin" in agent_name or "4500" in agent_name or "ott" in agent_name:
                    """
                    Push to SCC
                    """
                    self.logger.info("%s is core probe"%(agent_name))
                    if PUSH_ALARM_CORE:
                        self.logger.info("Push alarm to scc is active")
                        time.sleep(0.5)
                        snmp = Snmp(str(data["ip"]).replace(' ', ''))
                        alarm_status, msg = snmp.check_agent()
                        data = {
                            "ishost"            : False,
                            "queueServiceName"  : "Check_Agent_IPTV_Status",
                            "queueHost"         : agent_name, 
                            "msg"               : str(msg),
                            "AlertStatus"       : alarm_status
                        }
                        self.logger.debug("alarm contain: %s"%(str(data)))
                        scc = Scc()
                        scc.post(data)
                    return HttpResponse(status=202)
                else:
                    self.logger.info("%s is not core probe"%(agent_name))
                    if PUSH_ALARM_PROBE:
                        self.logger.info("Push alarm to scc is active")
                        time.sleep(0.5)
                        snmp = Snmp(str(data["ip"]).replace(' ', ''))
                        alarm_status, msg = snmp.check_agent()
                        data = {
                            "ishost"            : False,
                            "queueServiceName"  : "Check_Agent_IPTV_Status",
                            "queueHost"         : agent_name, 
                            "msg"               : str(msg),
                            "AlertStatus"       : alarm_status
                        }
                        self.logger.debug("alarm contain: %s"%(str(data)))
                        scc = Scc()
                        scc.post(data)
                    return HttpResponse(status=202)
            else:
                self.logger.warning("Value not change: %s"%(str(pk)))
                return HttpResponse(status=400)
                # querry="update profile_agent set video=%s,last_update=unix_timestamp() where id=%s;"%(data['video'],pk)
                # RabbitMQQueue().push_query(querry)
                # return HttpResponse(status=202)
        #dropframe
        elif ('dropframe' in data) and len(data)==1:
            self.logger.debug("message: update dropframe -->%s"%(str(data)))
            querry="update profile_agent set dropframe=%s,last_update=unix_timestamp() where id=%s;"%(data['dropframe'],pk)
            RabbitMQQueue().push_query(querry)
            self.logger.info("message: update dropframe added to RabbitMQQueue: %s"%(querry))
            return HttpResponse(status=202)
        #discontinuity
        elif ('discontinuity' in data) and len(data)==1:
            self.logger.debug("message: update discontinuity -->%s"%(str(data)))
            querry="update profile_agent set discontinuity=%s,last_update=unix_timestamp() where id=%s;"%(data['discontinuity'],pk)
            RabbitMQQueue().push_query(querry)
            self.logger.info("message: update dropframe added to RabbitMQQueue: %s"%(querry))
            return HttpResponse(status=202)
        #analyzer_status
        elif ('analyzer_status' in data) and len(data)==1:
            self.logger.debug("message: update analyzer_status -->%s"%(str(data)))
            querry="update profile_agent set analyzer_status=%s,last_update=unix_timestamp() where id=%s;"%(data['analyzer_status'],pk)
            RabbitMQQueue().push_query(querry)
            self.logger.info("message: update dropframe added to RabbitMQQueue: %s"%(querry))
            return HttpResponse(status=202)
        return HttpResponse(status=400)

    @csrf_exempt
    def delete(self, request, pk):
        self.logger.info("Delete profile_agent_id: %s"%(str(pk)))
        profileAgent = self.get_object(pk)
        profileAgent.delete()
        self.logger.info("Success to delete profile_agent_id: %s"%(str(pk)))
        return HttpResponse(status=204)

