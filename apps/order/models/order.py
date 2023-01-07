# Django
from django.db import models

# Project
from core.base_model import BaseModel


class Order(BaseModel):
    NEW = 'new'
    PAID = 'paid'
    PACKAGING = 'packaging'
    DELIVER = 'deliver'
    DELIVERED = 'delivered'
    CANCELED = 'canceled'

    STRIPE = 'stripe'
    PAYPAL = 'paypal'
    STATUS = (
        (NEW, NEW),
        (PAID, PAID),
        (PACKAGING, PACKAGING),
        (DELIVER, DELIVER),
        (DELIVERED, DELIVERED),
        (CANCELED, CANCELED)
    )
    PAYMENT_TYPE = (
        (STRIPE, STRIPE),
        (PAYPAL, PAYPAL)
    )
    user = models.ForeignKey('user.User', on_delete=models.PROTECT, related_name='orders')
    status = models.CharField(max_length=9, choices=STATUS, default=NEW)
    payment_type = models.CharField(max_length=6, choices=PAYMENT_TYPE, null=True)
    total_price = models.DecimalField(max_digits=21, decimal_places=2, default=0)
    total_discount = models.DecimalField(max_digits=21, decimal_places=2, null=True)
    price_to_paid = models.DecimalField(max_digits=21, decimal_places=2, null=True)
    price_to_paid_with_tax = models.DecimalField(max_digits=21, decimal_places=2, null=True)
    dhl_tracking = models.CharField(max_length=63, null=True, blank=True)


class OrderProduct(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='products')
    product = models.ForeignKey('product.ProductVariant', on_delete=models.CASCADE, related_name='order_products')
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=21, decimal_places=2)
    discount_price = models.DecimalField(max_digits=21, decimal_places=2, null=True)
