# Rest-Framework
from rest_framework.generics import ListAPIView, RetrieveAPIView

# Project
from order.models import Order
from order.serializers.order_list import (
    OrderListSerializer,
    OrderAdminListSerializer,
    OrderDetailSerializer
)


class OrderListAPIView(ListAPIView):
    queryset = Order.objects.all().order_by('-id')
    serializer_class = OrderListSerializer
    filter_fields = ['status', ]

    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)
        return queryset.exclude(status=Order.NEW)


class OrderAdminListAPIView(ListAPIView):
    queryset = Order.objects.all().order_by('-id')
    serializer_class = OrderAdminListSerializer
    filter_fields = ['status', 'payment_type']

    def get_queryset(self):
        return self.queryset.exclude(status=Order.NEW)


class OrderDetailAPIVIew(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer
