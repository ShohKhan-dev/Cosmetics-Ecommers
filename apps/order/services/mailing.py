from sendgrid import SendGridAPIClient, Mail

from config.settings import SENDGRID_API_KEY, SEND_GRID_FROM_EMAIL
from order.models import Order


def send_email_after_paid_order(order_id: int):
    client = SendGridAPIClient(api_key=SENDGRID_API_KEY)

    order = Order.objects.get(id=order_id)
    address = order.user.addresses.filter(is_default=True)

    if address.exists():
        email = address.first().email
    else:
        email = order.user.addresses.first().email

    message = Mail(
        from_email=SEND_GRID_FROM_EMAIL,
        to_emails=email,
        subject='On-Cosmetics Order Link',
        html_content='You have successfully placed an order and here is a '
                     '<a href="https://on-cosmetics.vercel.app/my-orders">link</a> to your order.'
    )
    client.send(message)
