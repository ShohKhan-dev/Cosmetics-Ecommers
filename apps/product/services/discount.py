import os
from datetime import date

import django
from django.apps import apps
from django.db.models import Q

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
os.sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

Discount = apps.get_model(app_label='product', model_name='Discount')


def change_discount_status():
    today = date.today()
    # discount change status to active
    Discount.objects.filter(start_date__lte=today, end_date__gte=today, is_active=False).update(is_active=True)
    # discount change status to inactive
    Discount.objects.filter((Q(start_date__gt=today) | Q(end_date__lt=today)), is_active=True).update(is_active=False)
