# Generated by Django 4.0.2 on 2022-06-20 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_info', '0003_remove_companyinfo_coordinates'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyinfo',
            name='latitude',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='companyinfo',
            name='longitude',
            field=models.CharField(max_length=255, null=True),
        ),
    ]