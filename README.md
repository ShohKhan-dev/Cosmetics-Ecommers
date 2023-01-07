# PROJECT : e-commerce API 
![image](https://user-images.githubusercontent.com/44405438/170005691-5290fa19-6956-4d92-8389-52c12542b930.png)
![python](https://img.shields.io/badge/-python-grey?style=for-the-badge&logo=python&logoColor=white&labelColor=306998)
![django](https://img.shields.io/badge/-django-grey?style=for-the-badge&logo=django&logoColor=white&labelColor=092e20)
![postgresql](https://img.shields.io/badge/postgre-SQL-%23000.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![linux](https://img.shields.io/badge/linux-grey?style=for-the-badge&logo=linux&logoColor=white&labelColor=072c61)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)

### Language: python 3.8 +

### Frameworks : Django 4+, DjangoRestFramework 3.12 +

### Deployment: gunicorn, gitlab ci/cd , supervisord

### Database : postgresql 12+

# Project Setup

#### Create Database

```bash
>>> create role cosmetic_user with login password 'cosmetic_password';
>>> create database cosmetic with owner ecommerce_user;
```

#### Django install

```bash
>>> git clone 
>>> virtualenv .venv
>>> source .venv/bin/activate
>>> source conf
>>> pip install -r requirements.txt
>>> python manage.py migrate
```

# Architecture

```
.
└── apps
    └── app_name
        ├──  migrations
        ├──  __init__.py
        ├──  admin.py
        ├──  apps.py
        ├──  models.py
        ├──  serializer.py
        ├──  service.py
        ├──  tests.py
        ├──  urls.py
        ├──  views.py
    └──  config
        ├──  __init__.py
        ├──  asgi.py
        ├──  urls.py
        ├──  settings.py
        ├──  wsgi.py
        
    ├── .gitignore
    ├── .gitlab-ci.yml
    ├──  manage.py
    ├──  requirements.txt
```

### models.py

```python
from core.base_model import BaseModel
from django.db import models


class MyModel(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
```

### serializer.py

```python
from rest_framework import serializers


class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'my_model'
        fields = '__all__'  # or ['id', 'name']


class CustomSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()

```

### service.py

```python
from rest_framework.response import Response


def my_service(name: str):
    """business logicians"""
    return Response({'detail': 'successfully'}, status=200)
```

### views.py

```python
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView


class MyModelView(ModelViewSet):
    queryset = 'my_queryset'
    serializer_class = 'my_serializer_class'


class MyView(APIView):
    def post(self, request):
        serializer = 'my_serializer(request.data)'
        'serializer.is_valid(raise_exception=True)'
        return 'my_service(**serializer.validated_data)'
```

### urls.py

```python
from django.urls import path

'from .views import MyView'

urlpatterns = [
    path('my_view/', 'MyView.as_view()')
]
```

### main.urls.py

```python
from django.urls import path, include

urlpatterns = [
    path('/api/v1/{app_name}/', include('{app_name.urls}'))
]
```
