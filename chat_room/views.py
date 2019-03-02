from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from chat_room.models import Room, Chat
from chat_room.serializers import RoomSerializers#, ChatSerializers, ChatPostSerializers,  UserSerializer)


class Rooms(APIView):
    """Комнаты чата"""
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        rooms = Room.objects.all()#filter(Q(creater=request.user) | Q(invited=request.user))
        serializer = RoomSerializers(rooms, many=True)
        return Response({"data": serializer.data})

    # def post(self, request):
    #     Room.objects.create(creater=request.user)
    #     return Response(status=201)

