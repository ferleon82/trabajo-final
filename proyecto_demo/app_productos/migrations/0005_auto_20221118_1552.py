# Generated by Django 3.0 on 2022-11-18 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_productos', '0004_stock_fk_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
