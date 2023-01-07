# Generated by Django 4.0.2 on 2022-06-07 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_remove_productvariant_attributes_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attribute',
            old_name='name_de',
            new_name='name_uz',
        ),
        migrations.RenameField(
            model_name='attributevalue',
            old_name='value_de',
            new_name='value_uz',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='name_de',
            new_name='name_uz',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name_de',
            new_name='name_uz',
        ),
        migrations.RenameField(
            model_name='productvariant',
            old_name='characteristics_de',
            new_name='characteristics_uz',
        ),
        migrations.RenameField(
            model_name='productvariant',
            old_name='description_de',
            new_name='description_uz',
        ),
        migrations.RenameField(
            model_name='productvariant',
            old_name='name_de',
            new_name='name_uz',
        ),
    ]