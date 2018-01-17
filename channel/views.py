import json
from channel.models import *
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

#######################################################################
#                                                                     #
#-------------------------------cHANNEL-------------------------------#
#                                                                     #
#######################################################################
class ChannelList:
    """
    List all snippets, or create a new snippet.
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
            channel_list = Channel.objects.all()
        except Exception as e:
            args["detail"] = e
        if channel_list:
            args_channel_list=[]
            for channel in channel_list:
                args_channel_list.append({ 
                    'id'            : int(channel.id),
                    'name'          : channel.name,
                    'descr'         : channel.descr,
                    'group_id'      : int(channel.group_id),
                    'active'        : int(channel.active)
                    })
            args["detail"] = "OK"
            args["channel_list"] = args_channel_list
        else:
            args["detail"] = "Empty"
        data = json.dumps(args)
        return HttpResponse(data, content_type='application/json', status=200)

    def post(self, request, format=None):
        return HttpResponse(status=400)

class ChannelDetail:
    """
    Retrieve, update or delete a snippet instance.
    """
    @csrf_exempt
    def routing(self, request, pk):
        if request.method == "GET":
            return self.get(request, pk)
        elif request.method == "PUT":
            return self.put(request, pk)
        elif request.method == "DELETE":
            return self.delete(request, pk)

    def get_object(self, pk):
        try:
            return Channel.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return None

    def get(self, request, pk, format=None):
        args = {}
        channel = self.get_object(pk)
        if channel:
            args_channel = []
            args_channel.append({ 
                'id'            : int(channel.id),
                'name'          : channel.name,
                'descr'         : channel.descr,
                'group_id'      : int(channel.group_id),
                'active'        : int(channel.active)
            })
            args["detail"] = 'OK'
            args['channel'] = args_channel
        else:
            args["detail"] = 'Not found.'
        data = json.dumps(args)
        return HttpResponse(data, content_type='application/json', status=200)

    def put(self, request, pk, format=None):
        return HttpResponse(status=400)

    def delete(self, request, pk, format=None):
        return HttpResponse(status=204)



#######################################################################
#                                                                     #
#-------------------------------GROUP---------------------------------#
#                                                                     #
#######################################################################

class GroupList:
    """
    List all snippets, or create a new snippet.
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
            group_list = Group.objects.all()
        except Exception as e:
            args["detail"] = e
        if group_list:
            args_group_list=[]
            for group in group_list:
                args_group_list.append({ 
                    'id'            : int(group.id),
                    'name'          : group.name
                    })
            args["detail"] = "OK"
            args["group_list"] = args_group_list
        else:
            args["detail"] = "Empty"
        data = json.dumps(args)
        return HttpResponse(data, content_type='application/json', status=200)

    def post(self, request, format=None):
        return HttpResponse(status=400)

class GroupDetail:
    """
    Retrieve, update or delete a snippet instance.
    """
    @csrf_exempt
    def routing(self, request, pk):
        if request.method == "GET":
            return self.get(request, pk)
        elif request.method == "PUT":
            return self.put(request, pk)
        elif request.method == "DELETE":
            return self.delete(request, pk)

    def get_object(self, pk):
        try:
            return Group.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return None

    def get(self, request, pk, format=None):
        args = {}
        group = self.get_object(pk)
        if group:
            args_group = []
            args_group.append({ 
                'id'            : int(group.id),
                'name'          : group.name
            })
            args["detail"] = 'OK'
            args['group'] = args_group
        else:
            args["detail"] = 'Not found.'
        data = json.dumps(args)
        return HttpResponse(data, content_type='application/json', status=200)

    def put(self, request, pk, format=None):
        return HttpResponse(status=400)

    def delete(self, request, pk, format=None):
        return HttpResponse(status=204)

#######################################################################
#                                                                     #
#-------------------------------PROFILE-------------------------------#
#                                                                     #
#######################################################################


class ProfileList:
    """
    List all snippets, or create a new snippet.
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
            profile_list = Profile.objects.all()
        except Exception as e:
            args["detail"] = e

        if profile_list:
            args_profile_list=[]
            for profile in profile_list:
                args_profile_list.append({ 
                    'id'            : int(profile.id),
                    'ip'            : profile.ip,
                    'descr'         : profile.descr,
                    'status'        : int(profile.status),
                    'type'          : profile.type,
                    'channel'       : profile.channel_id,
                    'protocol'      : profile.protocol,
                    'monitor'       : profile.monitor,
                    'last_update'   : profile.last_update,
                    'active'        : profile.active
                    })
            args["detail"] = "OK"
            args["profile_list"] = args_profile_list
        else:
            args["detail"] = "Empty"
        data = json.dumps(args)
        return HttpResponse(data, content_type='application/json', status=200)

    def post(self, request, format=None):
        return HttpResponse(status=400)

class ProfileDetail:
    """
    Retrieve, update or delete a snippet instance.
    """
    @csrf_exempt
    def routing(self, request, pk):
        if request.method == "GET":
            return self.get(request, pk)
        elif request.method == "PUT":
            return self.put(request, pk)
        elif request.method == "DELETE":
            return self.delete(request, pk)

    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return None

    def get(self, request, pk, format=None):
        args = {}
        profile = self.get_object(pk)
        if profile:
            args_profile = []
            args_profile.append({ 
                'id'            : int(profile.id),
                'ip'            : profile.ip,
                'descr'         : profile.descr,
                'status'        : int(profile.status),
                'type'          : profile.type,
                'channel'       : profile.channel_id,
                'protocol'      : profile.protocol,
                'monitor'       : profile.monitor,
                'last_update'   : profile.last_update,
                'active'        : profile.active
            })
            args["detail"] = 'OK'
            args['profile'] = args_profile
        else:
            args["detail"] = 'Not found.'
        data = json.dumps(args)
        return HttpResponse(data, content_type='application/json', status=200)


    def put(self, request, pk, format=None):
        return HttpResponse(status=400)

    def delete(self, request, pk, format=None):
        return HttpResponse(status=204)



#######################################################################
#                                                                     #
#-----------------------------PROFILE GROUP---------------------------#
#                                                                     #
#######################################################################

class ProfileGroupList:
    """
    List all snippets, or create a new snippet.
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
            profileGroup_list = ProfileGroup.objects.all()
        except Exception as e:
            args["detail"] = e
        if profileGroup_list:
            args_profileGroup_list=[]
            for profileGroup in profileGroup_list:
                args_profileGroup_list.append({ 
                    'id'            : int(profileGroup.id),
                    'profile_id'    : int(profileGroup.profile_id),
                    'group_id'      : int(profileGroup.group_id)
                    })
            args["detail"] = "OK"
            args["profileGroup_list"] = args_profileGroup_list
        else:
            args["detail"] = "Empty"
        data = json.dumps(args)
        return HttpResponse(data, content_type='application/json', status=200)

    def post(self, request, format=None):
        return HttpResponse(status=400)

class ProfileGroupDetail:
    """
    Retrieve, update or delete a snippet instance.
    """
    @csrf_exempt
    def routing(self, request, pk):
        if request.method == "GET":
            return self.get(request, pk)
        elif request.method == "PUT":
            return self.put(request, pk)
        elif request.method == "DELETE":
            return self.delete(request, pk)

    def get_object(self, pk):
        try:
            return ProfileGroup.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return None

    def get(self, request, pk, format=None):
        args = {}
        profileGroup = self.get_object(pk)
        if profileGroup:
            args_profileGroup = []
            args_profileGroup.append({ 
                'id'            : int(profileGroup.id),
                'profile_id'    : int(profileGroup.profile_id),
                'group_id'      : int(profileGroup.group_id)
            })
            args["detail"] = 'OK'
            args['profileGroup'] = args_profileGroup
        else:
            args["detail"] = 'Not found.'
        data = json.dumps(args)
        return HttpResponse(data, content_type='application/json', status=200)

    def put(self, request, pk, format=None):
        return HttpResponse(status=400)

    def delete(self, request, pk, format=None):
        return HttpResponse(status=204)
