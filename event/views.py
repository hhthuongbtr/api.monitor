from event.models import *
from django.http import Http404, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from django.core.exceptions import ObjectDoesNotExist
from setting.DateTime import DateTime


#######################################################################
#                                                                     #
#-------------------------------EVENT---------------------------------#
#                                                                     #
#######################################################################
class EventList(APIView):
    """
    List all snippets, or create a new event.
    """
    def get(self, request, format=None):
        args = {}
        try:
            event_list = Event.objects.all()
        except Exception as e:
            args["detail"] = str(e)
            data = json.dumps(args)
            return HttpResponse(data, content_type='application/json', status=status.HTTP_200_OK)
        if event_list:
            args_event_list=[]
            for event in event_list:
                args_event_list.append(Event().parse_object_as_json_fortmat(event))
            args["detail"] = "OK"
            args["event_list"] = args_event_list
        else:
            args["detail"] = "Event is empty"
        data = json.dumps(args)
        return HttpResponse(data, content_type='application/json', status=status.HTTP_200_OK)

    def post(self, request, format=None):
        return Response(status=status.HTTP_400_BAD_REQUEST)

class EventDetail(APIView):
    """
    Retrieve, update or delete a event instance.
    """
    def get_object(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return None

    def get(self, request, pk, format=None):
        args = {}
        event = self.get_object(pk)
        if event:
            args_event = []
            args_event.append(Event().parse_object_as_json_fortmat(event))
            args["detail"] = 'OK'
            args['event'] = args_event
        else:
            args["detail"] = 'Not found.'
        data = json.dumps(args)
        return HttpResponse(data, content_type='application/json', status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        return Response(status=status.HTTP_204_NO_CONTENT)

#######################################################################
#                                                                     #
#------------------------------ENCODER--------------------------------#
#                                                                     #
#######################################################################
class EncoderList(APIView):
    """
    List all snippets, or create a new encoder.
    """
    def get(self, request, format=None):
        args = {}
        try:
            encoder_list = Encoder.objects.all()
        except Exception as e:
            args["detail"] = str(e)
            data = json.dumps(args)
            return HttpResponse(data, content_type='application/json', status=status.HTTP_200_OK)
        if encoder_list:
            args_encoder_list=[]
            for encoder in encoder_list:
                args_encoder_list.append(Encoder().parse_object_as_json_fortmat(encoder))
            args["detail"] = "OK"
            args["encoder_list"] = args_encoder_list
        else:
            args["detail"] = "encoder is empty"
        data = json.dumps(args)
        return HttpResponse(data, content_type='application/json', status=status.HTTP_200_OK)

    def post(self, request, format=None):
        return Response(status=status.HTTP_400_BAD_REQUEST)

class EncoderDetail(APIView):
    """
    Retrieve, update or delete a encoder instance.
    """
    def get_object(self, pk):
        try:
            return Encoder.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return None

    def get(self, request, pk, format=None):
        args = {}
        encoder = self.get_object(pk)
        if encoder:
            args_encoder = []
            args_encoder.append(Encoder().parse_object_as_json_fortmat(encoder))
            args["detail"] = 'OK'
            args['encoder'] = args_encoder
        else:
            args["detail"] = 'Not found.'
        data = json.dumps(args)
        return HttpResponse(data, content_type='application/json', status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        return Response(status=status.HTTP_204_NO_CONTENT)

#######################################################################
#                                                                     #
#------------------------------SERVICECHECK---------------------------#
#                                                                     #
#######################################################################
class ServiceCheckList(APIView):
    """
    List all snippets, or create a new encoder.
    """
    def get(self, request, format=None):
        args = {}
        try:
            service_check_list = ServiceCheck.objects.all()
        except Exception as e:
            args["detail"] = str(e)
            data = json.dumps(args)
            return HttpResponse(data, content_type='application/json', status=status.HTTP_200_OK)
        if service_check_list:
            args_service_check_list=[]
            for service_check in service_check_list:
                args_service_check_list.append(ServiceCheck().parse_object_as_json_fortmat(service_check))
            args["detail"] = "OK"
            args["service_check_list"] = args_service_check_list
        else:
            args["detail"] = "service_check is empty"
        data = json.dumps(args)
        return HttpResponse(data, content_type='application/json', status=status.HTTP_200_OK)

    def post(self, request, format=None):
        return Response(status=status.HTTP_400_BAD_REQUEST)

class ServiceCheckDetail(APIView):
    """
    Retrieve, update or delete a encoder instance.
    """
    def get_object(self, pk):
        try:
            return ServiceCheck.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return None

    def get(self, request, pk, format=None):
        args = {}
        service_check = self.get_object(pk)
        if service_check:
            args_service_check = []
            args_service_check.append(ServiceCheck().parse_object_as_json_fortmat(service_check))
            args["detail"] = 'OK'
            args['service_check'] = args_service_check
        else:
            args["detail"] = 'Not found.'
        data = json.dumps(args)
        return HttpResponse(data, content_type='application/json', status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        return Response(status=status.HTTP_204_NO_CONTENT)

#######################################################################
#                                                                     #
#-----------------------------EVENTMONITOR----------------------------#
#                                                                     #
#######################################################################
class EventMonitorList(APIView):
    """
    List all snippets, or create a new encoder.
    """
    def get(self, request, format=None):
        args = {}
        try:
            event_monitor_list = EventMonitor.objects.all()
        except Exception as e:
            args["detail"] = str(e)
            data = json.dumps(args)
            return HttpResponse(data, content_type='application/json', status=status.HTTP_200_OK)
        if event_monitor_list:
            args_event_monitor_list=[]
            for event_monitor in event_monitor_list:
                args_event_monitor_list.append(EventMonitor().parse_object_as_json_fortmat(event_monitor))
            args["detail"] = "OK"
            args["event_monitor_list"] = args_event_monitor_list
        else:
            args["detail"] = "service_check is empty"
        data = json.dumps(args)
        return HttpResponse(data, content_type='application/json', status=status.HTTP_200_OK)

    def post(self, request, format=None):
        return Response(status=status.HTTP_400_BAD_REQUEST)

class EventMonitorDetail(APIView):
    """
    Retrieve, update or delete a encoder instance.
    """
    def get_object(self, pk):
        try:
            return EventMonitor.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return None

    def get(self, request, pk, format=None):
        args = {}
        event_monitor = self.get_object(pk)
        if event_monitor:
            args_event_monitor = []
            args_event_monitor.append(EventMonitor().parse_object_as_json_fortmat(event_monitor))
            args["detail"] = 'OK'
            args['event_monitor'] = args_event_monitor
        else:
            args["detail"] = 'Not found.'
        data = json.dumps(args)
        return HttpResponse(data, content_type='application/json', status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        data = json.loads(request.body)
        id = data['id']
        event_monitor = self.get_object(id)
        event_monitor.pid = data['pid']
        event_monitor.event_id = data['event_id']
        event_monitor.encoder_id = data['encoder_id']
        event_monitor.service_check_id = data['service_check_id']
        event_monitor.descr = data['descr']
        event_monitor.active = data['active']
        date_time = DateTime()
        now = date_time.get_now()
        event_monitor.last_update = now
        event_monitor.save()
        args_event_monitor = []
        args_event_monitor.append(EventMonitor().parse_object_as_json_fortmat(event_monitor))
        data = json.dumps(args_event_monitor)
        return HttpResponse(data, content_type='application/json', status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        return Response(status=status.HTTP_204_NO_CONTENT)

class MonitorList:
    def __init__(self):
        from BLL.event import Event as EventBLL
        self.event = EventBLL()

    def get_monitor_list(self, request):
        monitor_list = self.event.get_event_monitor_list()
        data = json.dumps(monitor_list)
        return HttpResponse(data, content_type='application/json', status=status.HTTP_200_OK)

    def get_running_monitor_list(self, request):
        running_monitor_list = self.event.get_running_event_monitor_list()
        data = json.dumps(running_monitor_list)
        return HttpResponse(data, content_type='application/json', status=status.HTTP_200_OK)

    def get_waiting_monitor_list(self, request):
        running_monitor_list = self.event.get_waiting_event_monitor_list()
        data = json.dumps(running_monitor_list)
        return HttpResponse(data, content_type='application/json', status=status.HTTP_200_OK)

    def get_completed_monitor_list(self, request):
        running_monitor_list = self.event.get_completed_event_monitor_list()
        data = json.dumps(running_monitor_list)
        return HttpResponse(data, content_type='application/json', status=status.HTTP_200_OK)

class MonitorDetail:
    def __init__(self):
        from BLL.event import Event as EventBLL
        self.event = EventBLL()

    def get_event_monitor(self, request, event_monitor_id):
        monitor = self.event.get_event_monitor(event_monitor_id)
        data = json.dumps(monitor)
        return HttpResponse(data, content_type='application/json', status=status.HTTP_200_OK)


