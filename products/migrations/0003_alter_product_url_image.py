# Generated by Django 4.1.2 on 2022-10-07 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_url_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='url_image',
            field=models.TextField(editable=False, max_length=6000),
        ),
    ]
