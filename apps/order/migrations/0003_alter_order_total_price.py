# Generated by Django 4.0.2 on 2022-07-13 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_payment_type_order_total_discount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=21),
        ),
    ]