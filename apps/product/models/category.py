from django.db import models
from core.base_model import BaseModel
# Create your models here.
from mptt.managers import TreeManager
from mptt.models import MPTTModel, TreeForeignKey


class CategoryManager(TreeManager):
    def viewable(self):
        queryset = self.get_queryset().filter(level=0)
        return queryset


class Category(MPTTModel, BaseModel):
    name = models.CharField(max_length=255)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    objects = CategoryManager()

    class MPTTMeta:
        order_insertion_by = ['name']
        
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
