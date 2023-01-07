from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView, Response
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from product.serializers.product import ProductSerializer, ProductVariantSerializer, ProductVariantCheckGetSerializer, \
    ProductVariantCheckPostSerializer
from product.models import Product, ProductVariant, AttributeValue, Attribute
from rest_framework.permissions import AllowAny
from product.filters import ProductVariantFilter


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [AllowAny]
        return super(ProductViewSet, self).get_permissions()


class ProductVariantViewSet(ModelViewSet):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product']


class ProductVariantListAPIView(ListAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantSerializer
    permission_classes = [AllowAny]
    filterset_class = ProductVariantFilter
    search_fields = ['name_en', 'name_de', 'name_ru', 'description_en', 'description_de', 'description_ru']
    ordering_fields = ['price', 'created_datetime']


class GetAttributeProductAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        results = []
        product = get_object_or_404(Product, pk=pk)
        product_variants = ProductVariant.objects.filter(product=product)
        attribute_values = AttributeValue.objects.filter(productvariant__in=product_variants)
        attributes = {}
        for attribute_value in attribute_values:
            if attribute_value.attribute.id not in attributes:
                attributes[attribute_value.attribute.id] = []
            if attribute_value.value not in attributes[attribute_value.attribute.id]:
                attributes[attribute_value.attribute.id].append({
                    'id': attribute_value.id,
                    'value_en': attribute_value.value_en,
                    'value_ru': attribute_value.value_ru,
                    'value_de': attribute_value.value_de,
                })
        for key, value in attributes.items():
            attribute = Attribute.objects.get(pk=key)
            results.append({
                'name_en': attribute.name_en,
                'name_ru': attribute.name_ru,
                'name_de': attribute.name_de,
                'values': value
            })
        return Response(results)


class ProductVariantCheckView(APIView):

    def post(self, request):
        serializer = ProductVariantCheckPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ids = serializer.data.get('id', [])
        product_variants = ProductVariant.objects.filter(id__in=ids)
        serializer = ProductVariantCheckGetSerializer(product_variants, many=True, context={'request': request})
        return Response(serializer.data)


__all__ = ['ProductViewSet', 'ProductVariantViewSet', 'ProductVariantListAPIView', 'GetAttributeProductAPIView']
