from django.db import models

from core.base_model import BaseModel


class FeedBack(BaseModel):
    username = models.CharField(max_length=31, blank=True)
    email = models.EmailField(max_length=31, blank=True)
    phone_number = models.CharField(max_length=31, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
