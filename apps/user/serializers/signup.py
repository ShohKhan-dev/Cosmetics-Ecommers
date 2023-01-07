# Rest-Framework
from rest_framework import serializers

# Project
from user.models import User


class SignupSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    user_type = serializers.ChoiceField(choices=User.TYPES)
    speciality = serializers.CharField(required=False)
    phone_number = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        if attrs['user_type'] == User.BEAUTICIAN and not attrs.get('speciality'):
            raise serializers.ValidationError(detail={'speciality': 'required filed'})
        return attrs


class CheckUsernameSerializer(serializers.Serializer):
    username = serializers.CharField()
