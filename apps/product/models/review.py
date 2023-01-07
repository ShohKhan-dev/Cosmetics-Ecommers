from django.db import models
from core.base_model import BaseModel
from django.core.validators import MaxValueValidator, MinValueValidator


class ProductReview(BaseModel):
    product = models.ForeignKey('ProductVariant', on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='reviews')
    content = models.TextField(blank=True, null=True)
    stars = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        ordering = ['-created_datetime']
        unique_together = ['product', 'user']
        verbose_name = 'Product Review'
        verbose_name_plural = 'Product Reviews'
