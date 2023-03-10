
# Generated by Django 4.0.2 on 2022-06-21 05:49


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_remove_product_variants_productvariant_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attribute',
            old_name='name_uz',
            new_name='name_de',
        ),
        migrations.RenameField(
            model_name='attributevalue',
            old_name='value_uz',
            new_name='value_de',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='name_uz',
            new_name='name_de',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name_uz',
            new_name='name_de',
        ),
        migrations.RenameField(
            model_name='productvariant',
            old_name='characteristics_uz',
            new_name='characteristics_de',
        ),
        migrations.RenameField(
            model_name='productvariant',
            old_name='description_uz',
            new_name='description_de',
        ),
        migrations.RenameField(
            model_name='productvariant',
            old_name='name_uz',
            new_name='name_de',
        ),
    ]
