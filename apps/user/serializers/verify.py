# Rest-Framework
from rest_framework import serializers


class UserVerifySerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField()


class ReSendVerifyUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
