# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-09 11:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printer', '0004_auto_20161108_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseprinter',
            name='info_consumables',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='информация по расходникам'),
        ),
    ]
