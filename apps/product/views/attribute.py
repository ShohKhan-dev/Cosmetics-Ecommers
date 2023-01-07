from rest_framework.viewsets import ModelViewSet
from product.serializers.attribute import AttributeSerializer, AttributeValueSerializer
from product.models.attribute import Attribute, AttributeValue
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from product.models.category import Category
from product.models.product import ProductVariant
from product.serializers.attribute import AttributeFilterSerializer
from rest_framework import status
from rest_framework.response import Response


class AttributeViewSet(ModelViewSet):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer


class AttributeValueViewSet(ModelViewSet):
    queryset = AttributeValue.objects.all()
    serializer_class = AttributeValueSerializer
    filter_fields = ['attribute']


class AttributeFilterView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        category_id = request.query_params.get('category_id')
        if category_id:
            category = Category.objects.get(id=category_id)
            if category.is_root_node() is True:
                categories = category.get_descendants(
                    include_self=True,
                )
            else:
                categories = [category]
            attribute_value_ids = set(
                ProductVariant.objects.filter(product__category__in=categories).values_list(
                    'attribute_values',
                    flat=True,
                ))
            attribute_value_queryset = AttributeValue.objects.filter(id__in=attribute_value_ids)
            attribute_ids = set(attribute_value_queryset.values_list('attribute', flat=True))
            attributes = Attribute.objects.filter(id__in=attribute_ids)
            serializer = AttributeFilterSerializer(attributes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        serializer = AttributeFilterSerializer(Attribute.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


__all__ = ['AttributeViewSet', 'AttributeValueViewSet', 'AttributeFilterView']
