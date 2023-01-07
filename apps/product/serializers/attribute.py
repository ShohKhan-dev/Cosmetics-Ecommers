from rest_framework import serializers
from product.models.attribute import Attribute, AttributeValue


class AttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeValue
        exclude = ('created_datetime', 'modified_datetime')
        extra_kwargs = {
            'attribute': {'required': True},
            'value': {'required': False},
        }


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        exclude = ('created_datetime', 'modified_datetime')
        extra_kwargs = {
            'name': {'required': False},
        }


class AttributeFilterSerializer(serializers.ModelSerializer):
    values = serializers.SerializerMethodField()

    class Meta:
        model = Attribute
        fields = [
            'id',
            'name',
            'values'
        ]

    def get_values(self, instance):
        queryset = instance.attributevalue_set.all()
        serializer = AttributeValueSerializer(queryset, many=True)
        return serializer.data


class SelectAttributeValue(serializers.ModelSerializer):
    attribute = AttributeSerializer()

    class Meta:
        model = AttributeValue
        exclude = ('created_datetime', 'modified_datetime')
