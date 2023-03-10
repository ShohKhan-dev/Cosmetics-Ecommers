# Generated by Django 4.0.2 on 2022-08-12 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_address_zip_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('modified_datetime', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'ordering': ('-created_datetime',),
            },
        ),
    ]
