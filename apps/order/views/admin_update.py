# Rest-Framework
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser

# Project
from order.serializers.admin_update import UpdateOrderStatusSerializer
from order.services.admin_update import update_order_status


class AdminUpdateOrderStatusView(APIView):
    permission_classes = [IsAdminUser, ]

    def post(self, request):
        serializer = UpdateOrderStatusSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return update_order_status(**serializer.validated_data)
