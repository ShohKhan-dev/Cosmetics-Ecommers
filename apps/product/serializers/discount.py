from rest_framework import serializers
from product.models import *
from product.serializers.product import ProductSerializer, ProductVariantListSerializer
from product.utils.discount_validators import discount_validators


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        exclude = ('created_datetime', 'modified_datetime')

    def validate(self, attrs):
        discount_validators(self.context['request'], attrs)
        return super().validate(attrs)

    def to_representation(self, instance):
        self.fields['products'] = ProductSerializer(many=True, context=self.context)
        self.fields['product_variants'] = ProductVariantListSerializer(many=True, context=self.context)
        return super(DiscountSerializer, self).to_representation(instance)
