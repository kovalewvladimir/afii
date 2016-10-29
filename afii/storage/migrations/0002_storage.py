# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-29 12:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('space', '0002_space'),
        ('storage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='имя')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='storage', to='space.Space', verbose_name='площадка')),
            ],
            options={
                'verbose_name_plural': 'склад',
                'verbose_name': 'склад',
            },
        ),
    ]
