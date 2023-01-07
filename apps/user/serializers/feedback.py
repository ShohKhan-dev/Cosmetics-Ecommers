from rest_framework import serializers
from user.models import FeedBack


class FeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBack
        exclude = ('created_datetime', 'modified_datetime')

    def create(self, validated_data):
        user = self.context['request'].user
        if user.is_authenticated:
            validated_data['username'] = user.username
            validated_data['email'] = user.email
            validated_data['phone_number'] = user.phone_number
            data = FeedBack.objects.create(**validated_data)
        else:
            data = FeedBack.objects.create(**validated_data)
        return data


__all__ = ['FeedBackSerializer']
