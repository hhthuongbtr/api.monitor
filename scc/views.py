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
        json_data = json.loads(request.body)
        if request.method  == "POST":
            return self.post(json_data, request)

    @csrf_exempt
    def post(self, json_data, request = None):
        scc = SccBLL()
        rsp = scc.post(json_data)
        data = json.dumps(rsp.json())
        if request:
            return HttpResponse(data, content_type='application/json', status=status.HTTP_200_OK)
        return rsp.json()

