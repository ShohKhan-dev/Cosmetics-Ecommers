# Python
from random import randint

# Rest-Framework
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# Mail
from config.settings import SENDGRID_API_KEY, SEND_GRID_FROM_EMAIL
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Project
from user.models import VerifyUser, User


def send_email_code(email: str, code: str, subject: str):
    client = SendGridAPIClient(api_key=SENDGRID_API_KEY)
    message = Mail(
        from_email=SEND_GRID_FROM_EMAIL,
        to_emails=email,
        subject=subject,
        plain_text_content=str(code)
    )
    client.send(message)


def send_user_verify_code(user, is_forgot_password=False):
    code = randint(100_000, 999_999)
    if is_forgot_password is False:
        VerifyUser.objects.create(
            user=user,
            code=f'verify_username_{code}',
            is_active=False
        )
    elif is_forgot_password is True:
        VerifyUser.objects.create(
            user=user,
            code=f'forgot_password_{code}',
            is_active=False
        )
    send_email_code(
        user.email, code, 'Verification email',
    )


def check_verify_signup_code(email, code):
    check = VerifyUser.objects.filter(
        user__email=email,
        code=f'verify_username_{code}',
        is_active=False
    )
    if check.exists():
        verify = check.first()
        verify.is_active = True
        verify.save()
        user = verify.user
        user.is_active = True
        user.save()

        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    else:
        return Response({'detail': 'invalid code'}, status=status.HTTP_400_BAD_REQUEST)


def check_verify_forgot_password_code(email, code):
    check = VerifyUser.objects.filter(
        user__email=email,
        code=f'forgot_password_{code}',
        is_active=False
    )
    return check.exists()


def re_send_verify_user_code(email):
    try:
        user = User.objects.get(email=email)
        send_user_verify_code(user)
        return Response({'detail': 'successfully send new code'})
    except User.DoesNotExist:
        return Response({'detail': 'username does not exist'}, status=status.HTTP_400_BAD_REQUEST)
