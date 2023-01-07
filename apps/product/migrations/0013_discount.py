# Generated by Django 4.0.2 on 2022-07-20 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_merge_20220627_0816'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('modified_datetime', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('percent', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('amount', models.PositiveIntegerField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('product_variants', models.ManyToManyField(blank=True, related_name='discounts', to='product.ProductVariant')),
                ('products', models.ManyToManyField(blank=True, related_name='discounts', to='product.Product')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]