from rest_framework.viewsets import ModelViewSet
from product.serializers.discount import DiscountSerializer
from product.models import Discount


class DiscountViewSet(ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
