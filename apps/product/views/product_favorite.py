from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from product.models import ProductFavorite, ProductVariant
from apps.product.serializers.product import ProductFavoriteSerializer
from rest_framework import serializers
from rest_framework import generics


class ProductFavoriteAPIView(APIView):
    def get(self, request, pk):
        get_object_or_404(ProductVariant, pk=pk)
        favorite = ProductFavorite.objects.filter(product_variant=pk, user=request.user)
        if favorite.exists():
            favorite.delete()
            return Response({'detail': 'removed !'})
        else:
            ProductFavorite.objects.create(product_variant_id=pk, user=request.user)
            return Response({'detail': 'added !'})


class ProductFavoriteListAPIView(generics.ListAPIView):
    serializer_class = ProductFavoriteSerializer

    def get_queryset(self):
        user = self.request.user
        return ProductFavorite.objects.filter(user=user)


__all__ = ['ProductFavoriteAPIView', 'ProductFavoriteListAPIView']
