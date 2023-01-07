from django.db import models
from core.base_model import BaseModel


class Attribute(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class AttributeValue(BaseModel):
    value = models.CharField(max_length=255)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.attribute.name}: {self.value}' if self.attribute else self.value
