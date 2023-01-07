from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from product.serializers.category import CategorySerializer, CategoryListSerializer
from product.models.category import Category


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    search_fields = ['name_en', 'name_de', 'name_ru']


class CategoryListViewSet(ModelViewSet):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.viewable()
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('name',)
    permission_classes = [AllowAny]


__all__ = ['CategoryViewSet', 'CategoryListViewSet']
