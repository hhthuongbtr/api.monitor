from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
import json
from BLL.scc import Scc as SccBLL
# from accounts.user_info import *


#######################################################################
#                                                                     #
#-------------------------------SCC-----------------------------------#
#                                                                     #
#######################################################################
class Scc:
    """
    List all events, or create a new event.
    """
    @csrf_exempt
    def routing(self, request):
        if request.method  == "POST":
            return self.http_post(request)

    @csrf_exempt
    def post(self, json_data):
        scc = SccBLL()
        rsp = scc.post(json_data)
        data = json.dumps(rsp.json())
        return rsp.json()

    @csrf_exempt
    def http_post(self, request):
        try:
            json_data = json.loads(request.body)
        except Exception as e:
            print e
            return HttpResponse(status=400)
        try:
            json_data['AlertStatus']
        except Exception as e:
            json_data = json.loads(json_data)
        scc = SccBLL()
        rsp = scc.post(json_data)
        print rsp.json()
        data = json.dumps(rsp.json())
        return HttpResponse(data, content_type='application/json', status=202)

