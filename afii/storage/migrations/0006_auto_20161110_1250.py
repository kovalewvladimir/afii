# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-10 09:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0005_auto_20161110_1028'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itemstorage',
            options={'verbose_name': 'единицу складского учета', 'verbose_name_plural': 'единица складского учета'},
        ),
        migrations.RemoveField(
            model_name='itemstorage',
            name='delete',
        ),
        migrations.AddField(
            model_name='itemstorage',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='используется'),
        ),
        migrations.AlterField(
            model_name='category',
            name='base_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='storage.Category', verbose_name='базовая категория'),
        ),
        migrations.AlterField(
            model_name='category',
            name='storage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='storage.Storage', verbose_name='склад'),
        ),
        migrations.AlterField(
            model_name='itemstorage',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='storage.Category', verbose_name='категория'),
        ),
    ]
