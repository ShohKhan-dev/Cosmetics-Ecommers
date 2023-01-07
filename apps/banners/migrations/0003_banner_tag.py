# Generated by Django 4.0.2 on 2022-08-12 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banners', '0002_alter_banner_options_banner_description_de_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='tag',
            field=models.CharField(choices=[('brand', 'brand'), ('about', 'about'), ('faq', 'faq'), ('contact', 'contact')], default='home', max_length=15),
        ),
    ]