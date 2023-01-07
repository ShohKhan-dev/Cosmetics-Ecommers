# Rest-Framework
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

# Stripe
import stripe
from stripe.error import SignatureVerificationError

# Project
from django.conf import settings

from order.models import Order
from payment.services.stripe.transaction import create_stripe_transaction, create_stripe_order_transaction

stripe.api_key = settings.STRIPE_SECRET_KEY


class StripeCheckoutAPIView(APIView):
    permission_classes = [AllowAny, ]

    def post(self, request):
        try:
            order = Order.objects.get(user=request.user, status=Order.NEW)
            secret_key = create_stripe_transaction(amount=order.price_to_paid, order_id=order.id)
            return Response(data={'secret_key': secret_key})
        except stripe.error.InvalidRequestError as e:
            return Response(data={'detail': e.error}, status=400)
        except Order.DoesNotExist:
            return Response(data={'detail': 'order not found'}, status=400)


class StripeWebhookAPIView(APIView):
    permission_classes = [AllowAny]
    endpoint_secret = 'whsec_003697f7b51a718cc9b26c30d543a2e9916739657b0b66a68fe216cb3e78dfec'

    def post(self, request):
        payload = request.data
        event = payload
        # sig_header = request.headers['STRIPE_SIGNATURE']
        # try:
        #     event = stripe.Webhook.construct_event(
        #         payload, sig_header, self.endpoint_secret
        #     )
        # except ValueError as e:
        #     # Invalid payload
        #     raise e
        # except SignatureVerificationError as e: TODO fix SignatureVerificationError
        #     # Invalid signature
        #     raise e

        # Handle the event
        if event['type'] == 'payment_intent.canceled':
            payment_intent = event['data']['object']


        elif event['type'] == 'payment_intent.created':
            payment_intent = event['data']['object']


        elif event['type'] == 'payment_intent.payment_failed':
            payment_intent = event['data']['object']


        elif event['type'] == 'payment_intent.succeeded':
            payment_intent = event['data']['object']
            stripe_id = payment_intent['id']
            amount = payment_intent['amount']
            order_id = payment_intent['metadata']['order_id']
            create_stripe_order_transaction(stripe_id, amount, order_id)

        return Response(data={'detail': 'success'}, status=200)
