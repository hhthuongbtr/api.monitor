from channel.models import *
from channel.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


#######################################################################
#                                                                     #
#-------------------------------cHANNEL-------------------------------#
#                                                                     #
#######################################################################
class ChannelList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        channel = Channel.objects.all()
        serializer = ChannelSerializer(channel, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ChannelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ChannelDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Channel.objects.get(pk=pk)
        except Channel.DoesNotExist:
            return HttpResponse({detail: "Not found."}, content_type='application/json', status=status.HTTP_204_NO_CONTENT)

    def get(self, request, pk, format=None):
        channel = self.get_object(pk)
        serializer = ChannelSerializer(channel)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        channel = self.get_object(pk)
        serializer = ChannelSerializer(channel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            channel.last_update=int(time.time())
            channel.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        channel = self.get_object(pk)
        channel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#######################################################################
#                                                                     #
#-------------------------------GROUP---------------------------------#
#                                                                     #
#######################################################################

class GroupList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        group = Group.objects.all()
        serializer = GroupSerializer(group, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class GroupDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Group.objects.get(pk=pk)
        except Group.DoesNotExist:
            return HttpResponse({detail: "Not found."}, content_type='application/json', status=status.HTTP_204_NO_CONTENT)

    def get(self, request, pk, format=None):
        group = self.get_object(pk)
        serializer = GroupSerializer(group)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        group = self.get_object(pk)
        serializer = GroupSerializer(group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            group.last_update=int(time.time())
            group.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        group = self.get_object(pk)
        group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#######################################################################
#                                                                     #
#-------------------------------PROFILE-------------------------------#
#                                                                     #
#######################################################################


class ProfileList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ProfileDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return HttpResponse({detail: "Not found."}, content_type='application/json', status=status.HTTP_204_NO_CONTENT)

    def get(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            profile.last_update=int(time.time())
            profile.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profile = self.get_object(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#######################################################################
#                                                                     #
#-----------------------------PROFILE GROUP---------------------------#
#                                                                     #
#######################################################################

class ProfileGroupList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        profileGroup = ProfileGroup.objects.all()
        serializer = ProfileGroupSerializer(profileGroup, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfileGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ProfileGroupDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return ProfileGroup.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return HttpResponse({detail: "Not found."}, content_type='application/json', status=status.HTTP_204_NO_CONTENT)

    def get(self, request, pk, format=None):
        profileGroup = self.get_object(pk)
        serializer = ProfileGroupSerializer(profileGroup)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        profileGroup = self.get_object(pk)
        serializer = ProfileGroupSerializer(profileGroup, data=request.data)
        if serializer.is_valid():
            serializer.save()
            profileGroup.last_update=int(time.time())
            profileGroup.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profileGroup = self.get_object(pk)
        profileGroup.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
