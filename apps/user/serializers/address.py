from rest_framework import serializers

from user.models.address import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"
        extra_kwargs = {'user': {'required': False}}

    def create(self, validated_data):
        addresses_count = Address.objects.filter(user=validated_data['user']).count()
        if addresses_count == 0:
            validated_data['is_default'] = True
        return super(AddressSerializer, self).create(validated_data)
