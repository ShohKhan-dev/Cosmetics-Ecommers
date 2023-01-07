from django.db import models
from core.base_model import BaseModel
from file.models import File


class Tag(BaseModel):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Blog(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ForeignKey(File, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title
