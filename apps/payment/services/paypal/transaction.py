# Paypal SDK
import paypalrestsdk

# Django
from django.conf import settings

# Project
from order.models import Order
from payment.services.paypal.utils import get_paypal_id_link
from transaction.models import OrderTransaction

PAYPAL_CLIENT_ID = settings.PAYPAL_CLIENT_ID
PAYPAL_SECRET_KEY = settings.PAYPAL_SECRET_KEY


def create_paypal_transaction(amount: int, order_id: int) -> str:
    paypal_api = paypalrestsdk.Api({
        'mode': 'sandbox',
        'client_id': PAYPAL_CLIENT_ID,
        'client_secret': PAYPAL_SECRET_KEY
    })

    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },
        "redirect_urls": {
            "return_url": f"{settings.FRONT_DOMAIN}?redirect_status=paypal_succeeded&order_id={order_id}",
            "cancel_url": f"{settings.FRONT_DOMAIN}?redirect_status=paypal_failed&order_id={order_id}"
        },
        "transactions": [
            {
                "amount": {
                    "total": int(amount * 100),
                    "currency": "USD"
                }
            }
        ]
    }, api=paypal_api)
    if payment.create() is True:
        paypal_id, paypal_url = get_paypal_id_link(payment)
        order = create_paypal_order_transaction(paypal_id, amount, order_id)
        if order is False:
            return False
        return paypal_url
    return False


def create_paypal_order_transaction(
        paypal_id: str,
        amount: int,
        order_id: str,
        status: str = OrderTransaction.PROCESSING
):
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return False
    OrderTransaction.objects.create(
        status=status,
        payment_type=OrderTransaction.PAYPAL,
        order=order,
        paypal_id=paypal_id,
        amount=amount
    )
    if status == OrderTransaction.SUCCESS:
        order.status = Order.PAID
    elif status == OrderTransaction.CANCELED:
        order.status = Order.CANCELED
    order.payment_type = Order.PAYPAL
    order.save(update_fields=['status', 'payment_type', 'modified_datetime'])
    return True


def update_paypal_order_transaction(order_id: int, status: str):
    try:
        order = Order.objects.get(id=order_id)
        order.status = status
        order.save(update_fields=['status', 'modified_datetime'])
    except Order.DoesNotExist:
        return False

    tr_status = OrderTransaction.SUCCESS if status == Order.PAID else OrderTransaction.CANCELED
    OrderTransaction.objects.filter(
        order=order, payment_type=OrderTransaction.PAYPAL, status=OrderTransaction.PROCESSING
    ).update(status=tr_status)
