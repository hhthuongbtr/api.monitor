import json
import logging
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from BLL import Scc as SccBLL


#######################################################################
#                                                                     #
#-------------------------------SCC-----------------------------------#
#                                                                     #
#######################################################################
class Scc:
    def __init__(self):
        self.logger = logging.getLogger("scc")

    @csrf_exempt
    def routing(self, request):
        if request.method  == "POST":
            return self.http_post(request)

    @csrf_exempt
    def post(self, data):
        json_data = json.loads(json.dumps(data))
        scc = SccBLL()
        rsp = scc.post(json_data)
        self.logger.debug("status: %d, message: %s"%(0, str(rsp)))
        return rsp.json()

    @csrf_exempt
    def http_post(self, request):
        try:
            json_data = json.loads(request.body)
        except Exception as e:
            self.logger.error("status: %d, message: %s"%(1, str(e)))
            return HttpResponse(status=400)
        try:
            json_data['AlertStatus']
        except Exception as e:
            self.logger.warning("status: %d, message: try json dump again, %s"%(1, str(e)))
            json_data = json.loads(json_data)
        scc = SccBLL()
        rsp = scc.post(json_data)
        self.logger.debug("status: %d, message: %s"%(0, str(rsp.json())))
        data = json.dumps(rsp.json())
        return HttpResponse(data, content_type='application/json', status=202)

