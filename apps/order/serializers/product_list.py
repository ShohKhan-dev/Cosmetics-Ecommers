# Rest-Framework
from rest_framework import serializers

# Project
from order.models import OrderProduct
from product.serializers.product import ProductVariantSerializer


class OrderProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = [
            'id',
            'product',
            'quantity',
            'total_price',
            'discount_price',
            'created_datetime'
        ]

    def to_representation(self, instance):
        self.fields['product'] = ProductVariantSerializer(context=self.context)
        return super(OrderProductListSerializer, self).to_representation(instance)
