from dataclasses import field

from django.db.models import Avg
from django.db.models.functions import Coalesce
from rest_framework import serializers
from product.models import *
from product.serializers import SelectAttributeValue
from product.services.product_variant import get_price_with_discount
from user.models import *
from file.serializers import FileSerializer, FileUrlSerializer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('created_datetime', 'modified_datetime')
        extra_kwargs = {
            'name': {'required': False},
        }

    def to_representation(self, instance):
        self.fields['image'] = FileUrlSerializer()
        return super(ProductSerializer, self).to_representation(instance)

    def update(self, instance, validated_data):

        if instance.is_available and validated_data.get("is_available"):
            ProductVariant.objects.filter(product=instance).update(is_available=False)
        if instance.is_available and validated_data.get("is_available"):
            ProductVariant.objects.filter(product=instance).update(is_available=True)

        return super().update(instance, validated_data)


class ProductVariantSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()
    price_with_discount = serializers.SerializerMethodField()

    class Meta:
        model = ProductVariant
        exclude = ('created_datetime', 'modified_datetime')

    def get_price(self, obj):
        user = self.context['request'].user
        return obj.price(user)

    def to_representation(self, instance):
        self.fields['images'] = FileSerializer(many=True, context=self.context)
        self.fields['attribute_values'] = SelectAttributeValue(many=True)
        return super(ProductVariantSerializer, self).to_representation(instance)

    def get_price_with_discount(self, obj):
        return get_price_with_discount(obj, user=self.context['request'].user)

    # def to_representation(self, instance):
    #     rep = super(ProductFavoriteSerializer, self).to_representation(instance)
    #     rep['id'] = instance.product_variant.id
    #     rep['name'] = instance.product_variant.name
    #     rep['image'] = instance.product_variant.product.image.file.url
    #     if instance.user.user_type == 'private':
    #         rep['price_for_private'] = instance.product_variant.price_for_private
    #     elif instance.user.user_type == 'entity':
    #         rep['price_for_entity'] = instance.product_variant.price_for_entity
    #     elif instance.user.user_type == 'beautician':
    #         rep['price_for_beautician'] = instance.product_variant.price_for_beautician
    #     return rep


class ProductVariantListSerializer(serializers.ModelSerializer):
    reviews_count = serializers.SerializerMethodField()
    reviews_avg = serializers.SerializerMethodField()
    price_with_discount = serializers.SerializerMethodField()
    price_in_som = serializers.IntegerField(read_only=True)

    class Meta:
        model = ProductVariant
        exclude = (
            'created_datetime',
            'modified_datetime',
        )

    def to_representation(self, instance):
        self.fields['images'] = FileSerializer(many=True, context=self.context)
        return super(ProductVariantListSerializer, self).to_representation(instance)

    def get_reviews_count(self, instance):
        return instance.reviews.count()

    def get_reviews_avg(self, instance):
        return instance.reviews.aggregate(avg_rate=Coalesce(Avg('stars'), 0.0))['avg_rate']

    def get_price_with_discount(self, obj):
        return get_price_with_discount(obj, user=self.context['request'].user)


class ProductFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFavorite
        fields = '__all__'


class ProductVariantCheckPostSerializer(serializers.Serializer):
    id = serializers.ListField(child=serializers.IntegerField())


class ProductVariantCheckGetSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()
    price_with_discount = serializers.SerializerMethodField()
    user_type = serializers.SerializerMethodField()

    class Meta:
        model = ProductVariant
        fields = (
            'id',
            'quantity',
            'is_available',
            'price',
            'price_with_discount',
            'user_type',
        )

    def get_user_type(self, obj):
        if self.context['request'].user.is_authenticated:
            return self.context['request'].user.user_type
        return None

    def get_price(self, obj):
        user = self.context['request'].user
        return obj.price(user)

    def get_price_with_discount(self, obj):
        return get_price_with_discount(obj, user=self.context['request'].user)
