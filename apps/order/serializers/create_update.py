# Rest-Framework
from rest_framework import serializers

# Project
from product.models import ProductVariant


class AddOrderProductSerializer(serializers.Serializer):
    product = serializers.PrimaryKeyRelatedField(queryset=ProductVariant.objects.all())
    quantity = serializers.IntegerField(min_value=1)


class UpdateOrderProductSerializer(serializers.Serializer):
    quantity = serializers.IntegerField(min_value=1)
