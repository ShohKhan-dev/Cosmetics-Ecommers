# Rest-Framework
from typing import Optional

from rest_framework.response import Response
from rest_framework import status

# Models
from user.models import User
from user.services.verify import send_user_verify_code


def check_username(username: str) -> bool:
    user = User.objects.filter(username__iexact=username).exists()
    return Response(data={'exists': user})


def signup(username: str, email: str, user_type: str, phone_number: str, password, speciality: Optional[str] = None):
    check_email = User.objects.filter(username__iexact=username).exists()
    if check_email is True:
        return Response({'detail': 'username already exists'}, status=status.HTTP_400_BAD_REQUEST)
    check_email = User.objects.filter(email=email).exists()
    if check_email is True:
        return Response({'detail': 'email already exists'}, status=status.HTTP_400_BAD_REQUEST)
    user = create_user(
        username=username,
        email=email,
        user_type=user_type,
        speciality=speciality,
        phone_number=phone_number,
        password=password
    )
    send_user_verify_code(user)
    return Response({'detail': 'successfully registered'}, status=status.HTTP_201_CREATED)


def create_user(
        username: str,
        email: str,
        user_type: str,
        phone_number: str,
        speciality: str = None,
        password=None
):
    user = User.objects.create(
        email=email,
        user_type=user_type,
        phone_number=phone_number,
        username=username,
        speciality=speciality,
        is_active=False,
        is_staff=False,
        is_superuser=False,
    )
    if password:
        user.set_password(password)
        user.save()
    return user
