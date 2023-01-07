# Rest-Framework
from rest_framework import serializers


class SendForgotPasswordCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()


class CheckForgotPasswordCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField()


class ForgotPasswordCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField()
    new_password = serializers.CharField()
