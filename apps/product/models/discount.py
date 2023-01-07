from datetime import date

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from core.base_model import BaseModel


class Discount(BaseModel):
    products = models.ManyToManyField('product.Product', related_name='discounts', blank=True)
    product_variants = models.ManyToManyField('product.ProductVariant', related_name='discounts', blank=True)
    name = models.CharField(max_length=100)
    percent = models.PositiveSmallIntegerField(blank=True, null=True)
    amount = models.PositiveIntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-id',)


@receiver(pre_save, sender=Discount)
def status(sender, instance, *args, **kwargs):
    today = date.today()
    if instance.start_date <= today <= instance.end_date:
        instance.is_active = True
    else:
        instance.is_active = False
