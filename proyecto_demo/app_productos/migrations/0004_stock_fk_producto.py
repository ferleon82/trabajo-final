# Generated by Django 3.0 on 2022-11-18 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_productos', '0003_auto_20221117_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='fk_producto',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app_productos.Producto'),
        ),
    ]
