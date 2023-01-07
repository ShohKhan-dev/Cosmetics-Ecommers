# Generated by Django 4.0.2 on 2022-09-08 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_subscription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='building_floor',
        ),
        migrations.RemoveField(
            model_name='address',
            name='building_number',
        ),
        migrations.RemoveField(
            model_name='address',
            name='street_home',
        ),
        migrations.AddField(
            model_name='address',
            name='company_name',
            field=models.CharField(blank=True, max_length=127, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='first_name',
            field=models.CharField(blank=True, max_length=127, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='house_number',
            field=models.CharField(default='1', max_length=31),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='is_different_shipping_address',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='address',
            name='last_name',
            field=models.CharField(blank=True, max_length=127, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='shipping_city',
            field=models.CharField(blank=True, max_length=127, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='shipping_company_name',
            field=models.CharField(blank=True, max_length=127, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='shipping_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='shipping_first_name',
            field=models.CharField(blank=True, max_length=127, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='shipping_house_number',
            field=models.CharField(blank=True, max_length=31, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='shipping_last_name',
            field=models.CharField(blank=True, max_length=127, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='shipping_phone_number',
            field=models.CharField(blank=True, max_length=31, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='shipping_region',
            field=models.CharField(blank=True, max_length=127, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='shipping_street_name',
            field=models.CharField(blank=True, max_length=127, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='shipping_zip_code',
            field=models.CharField(blank=True, max_length=31, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='street_name',
            field=models.CharField(default='test', max_length=127),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=127),
        ),
        migrations.AlterField(
            model_name='address',
            name='phone_number',
            field=models.CharField(max_length=31),
        ),
        migrations.AlterField(
            model_name='address',
            name='region',
            field=models.CharField(blank=True, max_length=127, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='zip_code',
            field=models.CharField(max_length=31),
        ),
    ]
