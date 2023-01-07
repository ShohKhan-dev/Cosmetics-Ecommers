from django.db import models

from core.base_model import BaseModel


class Subscription(BaseModel):
    email = models.EmailField()

    class Meta:
        ordering = ('-created_datetime',)

    def __str__(self):
        return self.email
