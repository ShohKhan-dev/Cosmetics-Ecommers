# Generated by Django 4.0.2 on 2022-08-09 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip_code',
            field=models.CharField(default=200100, max_length=32),
            preserve_default=False,
        ),
    ]
