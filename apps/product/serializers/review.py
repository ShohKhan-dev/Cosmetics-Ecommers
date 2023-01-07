from rest_framework import serializers
from product.models.review import ProductReview
from product.serializers.product import ProductVariantSerializer
from user.serializers.me import UserMeSerializer


class ProductReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        exclude = ('modified_datetime',)
        read_only_fields = ('user',)

    def validate(self, attrs):
        exists = ProductReview.objects.filter(user=self.context['request'].user, product=attrs.get('product')).exists()
        if exists:
            raise serializers.ValidationError('You have already reviewed this product')
        return attrs

    def to_representation(self, instance):
        self.fields['product'] = ProductVariantSerializer()
        self.fields['user'] = UserMeSerializer()
        return super(ProductReviewListSerializer, self).to_representation(instance)
