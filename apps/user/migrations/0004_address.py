# Generated by Django 4.0.2 on 2022-08-03 11:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_speciality'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('modified_datetime', models.DateTimeField(auto_now=True)),
                ('city', models.CharField(max_length=128)),
                ('region', models.CharField(max_length=128)),
                ('street_home', models.CharField(max_length=256)),
                ('building_number', models.IntegerField(blank=True, null=True)),
                ('building_floor', models.IntegerField()),
                ('phone_number', models.CharField(max_length=32)),
                ('is_default', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]