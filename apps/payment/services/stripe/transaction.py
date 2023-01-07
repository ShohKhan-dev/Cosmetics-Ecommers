# Stripe
import stripe

# Django
from django.conf import settings
from django.db import transaction

from order.services.mailing import send_email_after_paid_order
# Project
from transaction.models import OrderTransaction
from order.models import Order

stripe.api_key = settings.STRIPE_SECRET_KEY


def create_stripe_transaction(amount: int, order_id: int) -> str:
    return stripe.PaymentIntent.create(
        amount=int(amount * 100),
        currency='usd',
        metadata={
            'order_id': order_id
        },
        payment_method_types=['card']
    ).client_secret


@transaction.atomic
def create_stripe_order_transaction(stripe_id: str, amount: int, order_id: str):
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return False
    OrderTransaction.objects.create(
        status=OrderTransaction.SUCCESS,
        payment_type=OrderTransaction.STRIPE,
        order=order,
        stripe_id=stripe_id,
        amount=amount
    )
    order.status = Order.PAID
    order.payment_type = Order.STRIPE
    order.save(update_fields=['status', 'modified_datetime', 'payment_type'])
    send_email_after_paid_order(order_id=order_id)
    return True
