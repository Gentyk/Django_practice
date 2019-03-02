from rest_framework import serializers
from django.contrib.auth.models import User

from chat_room.models import Room, Chat


class UserSerializer(serializers.ModelSerializer):
    """Сериализация пользователя"""
    class Meta:
        model = User
        fields = ("id", "username")


class RoomSerializers(serializers.ModelSerializer):
    """Сериализация комнат чата"""
    creater = UserSerializer()
    invited = UserSerializer(many=True)
    class Meta:
        model = Room
        fields = ("id", "creater", "invited", "date")