# Django
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    PRIVATE = 'private'
    ENTITY = 'entity'
    BEAUTICIAN = 'beautician'
    TYPES = (
        (PRIVATE, PRIVATE),
        (ENTITY, ENTITY),
        (BEAUTICIAN, BEAUTICIAN)
    )
    user_type = models.CharField(max_length=20, choices=TYPES)
    speciality = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=50, null=True)
