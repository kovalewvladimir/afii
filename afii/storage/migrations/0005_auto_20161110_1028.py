# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-10 07:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0004_auto_20161110_1028'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='category',
            unique_together=set([('name', 'storage', 'base_category')]),
        ),
    ]
