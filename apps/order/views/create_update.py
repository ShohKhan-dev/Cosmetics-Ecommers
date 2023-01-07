# Rest-Framework
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

# Project
from order.models import OrderProduct
from order.serializers.create_update import AddOrderProductSerializer, UpdateOrderProductSerializer
from order.services.create_update import (
    add_order_product, update_order_product,
    delete_order_product, add_list_order_product
)


class AddOrderProductAPIView(APIView):
    serializer_class = AddOrderProductSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return add_order_product(user=request.user, **serializer.validated_data)


class AddListOrderProductAPIView(APIView):
    serializer_class = AddOrderProductSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        return add_list_order_product(user=request.user, products=serializer.validated_data)


class UpdateOrderProductAPIView(APIView):
    queryset = OrderProduct.objects.all()
    serializer_class = UpdateOrderProductSerializer

    def put(self, request, pk):
        instance = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return update_order_product(
            user=self.request.user, order_product=instance,
            **serializer.validated_data
        )


class DeleteOrderProductAPIView(APIView):
    queryset = OrderProduct.objects.all()

    def delete(self, request, pk):
        instance = get_object_or_404(self.queryset, pk=pk)
        return delete_order_product(self.request.user, instance)
