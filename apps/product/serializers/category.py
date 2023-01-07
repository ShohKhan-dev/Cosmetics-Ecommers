from rest_framework import serializers
from product.models.category import Category


class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('created_datetime', 'modified_datetime', 'lft', 'rght', 'tree_id', 'level')
        extra_kwargs = {
            'name': {'required': False},
        }


class CategoryListSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)

    class Meta:
        model = Category
        exclude = ('created_datetime', 'modified_datetime', 'lft', 'rght', 'tree_id', 'level')
