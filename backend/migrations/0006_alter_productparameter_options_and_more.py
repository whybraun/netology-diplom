# Generated by Django 5.0.4 on 2024-04-08 15:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_alter_productinfo_options_remove_productinfo_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productparameter',
            options={'verbose_name': 'Параметр', 'verbose_name_plural': 'Список параметров'},
        ),
        migrations.AlterField(
            model_name='productparameter',
            name='product_info',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_parameters', to='backend.productinfo', verbose_name='Информация о продукте'),
        ),
        migrations.AlterField(
            model_name='productparameter',
            name='value',
            field=models.CharField(max_length=100, verbose_name='Значение'),
        ),
    ]
