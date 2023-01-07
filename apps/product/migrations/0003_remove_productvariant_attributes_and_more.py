# Generated by Django 4.0.2 on 2022-06-06 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_remove_productvariant_product_product_variants'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productvariant',
            name='attributes',
        ),
        migrations.AddField(
            model_name='productvariant',
            name='attribute_values',
            field=models.ManyToManyField(to='product.AttributeValue'),
        ),
    ]