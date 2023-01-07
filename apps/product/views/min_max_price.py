from django.db.models import Min, Max
from rest_framework import permissions, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Category, ProductVariant


class GetMinMaxPriceView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        user_type = request.user.user_type if request.user.is_authenticated is True else 'private'
        category_id = request.query_params.get('category_id')
        product_variants = ProductVariant.objects.all()
        if category_id:
            category = get_object_or_404(Category, id=category_id)
            categories = category.get_descendants(include_self=True) if category.is_root_node() else [category]
            product_variants = product_variants.filter(product__category__in=categories)
        product_variants = product_variants.aggregate(
            min=Min(f"price_for_{user_type}"), max=Max(f"price_for_{user_type}")
        )
        return Response(product_variants)
