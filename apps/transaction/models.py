from django.db import models
from core.base_model import BaseModel


class OrderTransaction(BaseModel):
    PROCESSING = 'processing'
    SUCCESS = 'success'
    CANCELED = 'canceled'
    PAYPAL = 'paypal'
    STRIPE = 'stripe'

    STATUS = (
        (PROCESSING, PROCESSING),
        (SUCCESS, SUCCESS),
        (CANCELED, CANCELED)
    )
    PAYMENT_TYPES = (
        (PAYPAL, PAYPAL),
        (STRIPE, STRIPE)
    )

    status = models.CharField(max_length=20, choices=STATUS, default=PROCESSING)
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPES, default=STRIPE)
    amount = models.DecimalField(max_digits=21, decimal_places=2)
    order = models.ForeignKey('order.Order', on_delete=models.CASCADE)
    stripe_id = models.CharField(max_length=255, null=True)
    paypal_id = models.CharField(max_length=255, null=True)
