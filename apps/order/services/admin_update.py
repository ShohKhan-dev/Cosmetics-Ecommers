# Rest-Framework
from rest_framework.response import Response

# Project
from order.models import Order


def update_order_status(order: Order, status: str, dhl_tracking: str) -> Response:
    order.status = status
    order.dhl_tracking = dhl_tracking
    order.save(update_fields=['status', 'modified_datetime', 'dhl_tracking'])
    return Response(data={'detail': 'success'})
