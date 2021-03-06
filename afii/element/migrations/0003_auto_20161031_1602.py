# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('element', '0002_auto_20161031_1528'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='computer',
            options={'verbose_name': 'системный блок', 'verbose_name_plural': 'системные блоки'},
        ),
        migrations.AlterModelOptions(
            name='distribution',
            options={'verbose_name': 'дистрибутив', 'verbose_name_plural': 'дистрибутивы'},
        ),
        migrations.AlterModelOptions(
            name='paper',
            options={'verbose_name': 'бумага', 'verbose_name_plural': 'бумага'},
        ),
        migrations.AlterField(
            model_name='computer',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='используется'),
        ),
        migrations.AlterField(
            model_name='distribution',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='используется'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='используется'),
        ),
    ]
