from django.db import models
from core.base_model import BaseModel


class CompanyInfo(BaseModel):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=30)
    longitude = models.CharField(max_length=255, null=True)
    latitude = models.CharField(max_length=255, null=True)

    class Meta:
        verbose_name_plural = 'Company Infos'

    def __str__(self) -> str:
        return self.name