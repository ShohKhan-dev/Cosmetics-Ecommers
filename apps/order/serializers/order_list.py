# Rest-Framework
from rest_framework import serializers

# Project
from order.models import Order
from order.serializers.product_list import OrderProductListSerializer
from user.serializers.me import UserMeSerializer, UserAddressSerializer


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'status',
            'payment_type',
            'total_price',
            'total_discount',
            'price_to_paid',
            'price_to_paid_with_tax',
            "dhl_tracking",
            'created_datetime'
        ]


class OrderAdminListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['user'] = UserMeSerializer()
        return super(OrderAdminListSerializer, self).to_representation(instance)


class OrderDetailSerializer(serializers.ModelSerializer):
    user = UserAddressSerializer(read_only=True)
    products = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            'id',
            'status',
            'payment_type',
            'total_price',
            'total_discount',
            'price_to_paid',
            'price_to_paid_with_tax',
            'created_datetime',
            'products',
            "dhl_tracking",
            "user"
        ]

    def get_products(self, obj):
        serializer = OrderProductListSerializer(
            obj.products.all(), many=True, context=self.context
        )
        return serializer.data
