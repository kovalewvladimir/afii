# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-15 16:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0002_space'),
        ('element', '0004_distribution_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.PositiveIntegerField(verbose_name='длина')),
                ('description', models.TextField(blank=True, null=True, verbose_name='примечание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='cable/')),
                ('is_active', models.BooleanField(default=True, verbose_name='используется')),
                ('space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cable', to='space.Space', verbose_name='площадка')),
            ],
            options={
                'verbose_name_plural': 'кабеля',
                'verbose_name': 'кабель',
            },
        ),
        migrations.CreateModel(
            name='CableType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, verbose_name='тип кабеля')),
            ],
            options={
                'verbose_name_plural': 'Тип кабеля',
                'verbose_name': 'Тип кабель',
            },
        ),
        migrations.AddField(
            model_name='cable',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cable', to='element.CableType', verbose_name='тип кабеля'),
        ),
    ]
