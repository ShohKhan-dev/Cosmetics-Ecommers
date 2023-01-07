# Rest-Framework
from rest_framework import serializers

# Project
from order.models import Order


class UpdateOrderStatusSerializer(serializers.Serializer):
    STATUS = (
        (Order.PACKAGING, Order.PACKAGING),
        (Order.DELIVER, Order.DELIVER),
        (Order.DELIVERED, Order.DELIVERED),
        (Order.CANCELED, Order.CANCELED)
    )
    order = serializers.PrimaryKeyRelatedField(
        queryset=Order.objects.exclude(
            status__in=[Order.NEW, Order.CANCELED, Order.DELIVERED]
        )
    )
    status = serializers.ChoiceField(choices=STATUS)
    dhl_tracking = serializers.CharField(max_length=63, required=False)
