# Generated by Django 4.0.2 on 2022-09-08 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banners', '0003_banner_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='tag',
            field=models.CharField(choices=[('home', 'home'), ('brand', 'brand'), ('about', 'about'), ('faq', 'faq'), ('contact', 'contact'), ('product', 'product')], default='home', max_length=15),
        ),
    ]
