from django.db import models
from core.base_model import BaseModel
from file.models import File
from user.models import User


class Product(BaseModel):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ForeignKey(File, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=21, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ProductVariant(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price_for_private = models.DecimalField(max_digits=21, decimal_places=2)
    price_for_entity = models.DecimalField(max_digits=21, decimal_places=2)
    price_for_beautician = models.DecimalField(max_digits=21, decimal_places=2)
    images = models.ManyToManyField(File)
    characteristics = models.TextField()
    attribute_values = models.ManyToManyField('AttributeValue')
    is_available = models.BooleanField(default=True)
    quantity = models.IntegerField(default=0)

    def price(self, user):
        if user.is_authenticated is True:
            return getattr(self, f'price_for_{user.user_type}')
        return self.price_for_private


class ProductFavorite(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, related_name='product_variant')

    def __str__(self) -> str:
        return self.product_variant.name
