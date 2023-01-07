# Rest-Framework
from rest_framework.generics import ListAPIView

# Project
from order.models import OrderProduct, Order
from order.serializers.product_list import OrderProductListSerializer


class OrderProductListAPIVIew(ListAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductListSerializer

    def get_queryset(self):
        return self.queryset.filter(
            order__user=self.request.user,
            order__status=Order.NEW
        ).order_by('id')
