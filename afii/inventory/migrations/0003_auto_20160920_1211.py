# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 09:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20160920_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='base_categoty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Category'),
        ),
    ]
