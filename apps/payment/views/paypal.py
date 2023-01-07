# Rest-Framework
from django.db import transaction
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# Project
from order.models import Order
from order.services.mailing import send_email_after_paid_order
from payment.services.paypal.transaction import create_paypal_transaction, update_paypal_order_transaction


class PaypalCheckoutAPIView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        try:
            order = Order.objects.get(user=request.user, status=Order.NEW)
            approval_url = create_paypal_transaction(amount=order.price_to_paid, order_id=order.id)
            if approval_url is False:
                return Response(data={'detail': 'paypal error'}, status=400)
            return Response(data={'approval_url': approval_url})
        except Order.DoesNotExist:
            return Response(data={'detail': 'order not found'}, status=400)


class PaypalReturnAPIView(APIView):
    permission_classes = [AllowAny, ]

    @transaction.atomic
    def get(self, request, pk):
        update_paypal_order_transaction(pk, Order.PAID)
        send_email_after_paid_order(pk)
        return Response(data={'detail': 'success paid'})


class PaypalCancelAPIView(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request, pk):
        update_paypal_order_transaction(pk, Order.CANCELED)
        return Response(data={'detail': 'success canceled'})
