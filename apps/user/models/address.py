from django.db import models
from core.base_model import BaseModel
from user.models.base import User


class Address(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')

    first_name = models.CharField(max_length=127, null=True, blank=True)
    last_name = models.CharField(max_length=127, null=True, blank=True)
    company_name = models.CharField(max_length=127, null=True, blank=True)
    street_name = models.CharField(max_length=127)
    house_number = models.CharField(max_length=31)
    city = models.CharField(max_length=127)
    email = models.EmailField(null=True, blank=True)
    zip_code = models.CharField(max_length=31)
    phone_number = models.CharField(max_length=31)

    is_default = models.BooleanField(default=False)
    is_different_shipping_address = models.BooleanField(default=False)

    shipping_first_name = models.CharField(max_length=127, null=True, blank=True)
    shipping_last_name = models.CharField(max_length=127, null=True, blank=True)
    shipping_company_name = models.CharField(max_length=127, null=True, blank=True)
    shipping_street_name = models.CharField(max_length=127, null=True, blank=True)
    shipping_house_number = models.CharField(max_length=31, null=True, blank=True)
    shipping_city = models.CharField(max_length=127, null=True, blank=True)
    shipping_email = models.EmailField(null=True, blank=True)
    shipping_zip_code = models.CharField(max_length=31, null=True, blank=True)
    shipping_phone_number = models.CharField(max_length=31, null=True, blank=True)

    def __str__(self):
        return self.first_name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.is_different_shipping_address:
            self.shipping_first_name = self.first_name
            self.shipping_last_name = self.last_name
            self.shipping_company_name = self.company_name
            self.shipping_street_name = self.street_name
            self.shipping_house_number = self.house_number
            self.shipping_city = self.city
            self.shipping_email = self.email
            self.shipping_zip_code = self.zip_code
            self.shipping_phone_number = self.phone_number
        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
        ordering = ['-created_datetime']
