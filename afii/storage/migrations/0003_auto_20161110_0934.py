# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-10 06:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0002_space'),
        ('storage', '0002_storage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='имя')),
                ('is_base', models.BooleanField(default=False, verbose_name='базовая категория?')),
                ('base_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='storage.Category')),
            ],
            options={
                'verbose_name': 'категории',
                'verbose_name_plural': 'категория',
            },
        ),
        migrations.CreateModel(
            name='ItemStorage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='наименование')),
                ('count', models.PositiveIntegerField(verbose_name='кол-во')),
                ('shelf', models.CharField(max_length=10, verbose_name='№ полки')),
                ('delete', models.BooleanField(default=False, verbose_name='удален?')),
                ('image', models.ImageField(blank=True, null=True, upload_to='item_storage/')),
                ('description', models.TextField(blank=True, null=True, verbose_name='примечание')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='storage.Category')),
            ],
            options={
                'verbose_name': 'единица складского учета',
                'verbose_name_plural': 'единицу складского учета',
            },
        ),
        migrations.AlterUniqueTogether(
            name='storage',
            unique_together=set([('name', 'space')]),
        ),
        migrations.AddField(
            model_name='category',
            name='storage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='storage.Storage'),
        ),
        migrations.AlterUniqueTogether(
            name='itemstorage',
            unique_together=set([('name', 'category')]),
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together=set([('name', 'storage')]),
        ),
    ]
