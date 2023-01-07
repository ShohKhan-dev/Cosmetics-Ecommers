# Python
from datetime import datetime
from decimal import Decimal

# Django
from django.db.models import Sum, DecimalField
from django.db.models.functions import Coalesce

# Rest-Framework
from rest_framework import status
from rest_framework.response import Response

# Project
from user.models import User
from order.models import Order, OrderProduct
from product.models import ProductVariant
from product.models.discount import Discount


class NewOrderUserNotFound(Exception):
    pass


def get_new_order(func):
    def wrapper(*args, **kwargs):
        try:
            user: User = kwargs['user']
            order, _ = Order.objects.get_or_create(
                user=user, status=Order.NEW
            )
            kwargs['order'] = order
            return func(*args, **kwargs)
        except KeyError:
            raise NewOrderUserNotFound

    return wrapper


def calc_discount_total_price(product: ProductVariant, quantity: int, user: User):
    today = datetime.now().date()
    total_price = None
    product_price = getattr(product, f'price_for_{user.user_type}')
    product_discount = Discount.objects.filter(
        products__in=[product.product], start_date__lte=today, end_date__gte=today
    )
    variant_discount = Discount.objects.filter(
        product_variants__in=[product], start_date__lte=today, end_date__gte=today
    )
    discount = product_discount if product_discount.exists() else variant_discount
    if discount.exists():
        discount = discount.first()
        if discount.amount:
            total_price = discount.amount * quantity
        elif discount.percent:
            amount = product_price * discount.percent / 100
            total_price = amount * quantity

    return total_price


def calc_order_total_prices(order: Order):
    output_field = DecimalField(max_digits=21, decimal_places=2)
    products = OrderProduct.objects.filter(order=order)
    price = products.aggregate(sum_price=Coalesce(Sum('total_price'), 0, output_field=output_field))
    discount = products.aggregate(sum_discount=Coalesce(Sum('discount_price'), 0, output_field=output_field))
    order.total_price = price['sum_price']
    order.total_discount = discount['sum_discount']
    order.price_to_paid = order.total_price - order.total_discount
    order.price_to_paid_with_tax = order.price_to_paid * Decimal(1.19)
    order.save(update_fields=['total_price', 'total_discount', 'price_to_paid', 'price_to_paid_with_tax'])


@get_new_order
def add_order_product(
        user: User,
        product: ProductVariant,
        quantity: int,
        order: Order = None
) -> Response:
    """
    parm: order (decorator gives order)
    """
    product_price = getattr(product, f'price_for_{user.user_type}')
    if OrderProduct.objects.filter(order=order, product=product).exists():
        return Response(data={'detail': 'product already exists'}, status=status.HTTP_400_BAD_REQUEST)
    OrderProduct.objects.create(
        order=order, product=product, quantity=quantity, total_price=(product_price * quantity),
        discount_price=calc_discount_total_price(product, quantity, user)
    )
    calc_order_total_prices(order)
    return Response(data={'detail': f'successful added to user {user.id}'}, status=status.HTTP_200_OK)


@get_new_order
def add_list_order_product(
        user: User,
        products: list,
        order: Order = None
) -> Response:
    """
    parm: order (decorator gives order)
    """
    OrderProduct.objects.filter(order=order).delete()
    for or_product in products:
        product = or_product['product']
        product_price = getattr(product, f'price_for_{user.user_type}')
        OrderProduct.objects.create(
            order=order, product=product, quantity=or_product['quantity'],
            total_price=(product_price * or_product['quantity']),
            discount_price=calc_discount_total_price(product, or_product['quantity'], user)
        )
    calc_order_total_prices(order)
    return Response(data={'detail': f'successful added to user {user.id}'}, status=status.HTTP_200_OK)


def update_order_product(user: User, order_product: OrderProduct, quantity: int) -> Response:
    order = order_product.order
    product_price = getattr(order_product.product, f'price_for_{user.user_type}')
    if order.status != Order.NEW:
        return Response(data={'detail': 'you cannot change the order'}, status=status.HTTP_400_BAD_REQUEST)
    if user != order.user:
        return Response(data={'detail': 'you cannot change the order'}, status=status.HTTP_400_BAD_REQUEST)
    order_product.quantity = quantity
    order_product.total_price = (product_price * quantity)
    order_product.discount_price = calc_discount_total_price(order_product.product, quantity, user)
    order_product.save(
        update_fields=[
            'quantity', 'total_price',
            'discount_price', 'modified_datetime'
        ]
    )
    calc_order_total_prices(order)
    return Response(data={'detail': 'successful updated'}, status=status.HTTP_200_OK)


def delete_order_product(user: User, order_product: OrderProduct) -> Response:
    order = order_product.order
    if order.status != Order.NEW:
        return Response(data={'detail': 'you cannot change the order'}, status=status.HTTP_400_BAD_REQUEST)
    if user != order.user:
        return Response(data={'detail': 'you cannot change the order'}, status=status.HTTP_400_BAD_REQUEST)
    order_product.delete()
    calc_order_total_prices(order)
    return Response(data={'detail': 'successful deleted'}, status=status.HTTP_200_OK)
