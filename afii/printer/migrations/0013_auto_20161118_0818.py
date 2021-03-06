# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-18 05:18
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printer', '0012_auto_20161114_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartridge',
            name='shelf',
            field=models.CharField(help_text='<стеллаж>-<ярус> например: D-1', max_length=10, validators=[django.core.validators.RegexValidator(message='стеллаж - заглавная латинская буква, ярус - цифра', regex='^[A-Z]\\-[0-9]$')], verbose_name='№ полки'),
        ),
        migrations.AlterField(
            model_name='printer',
            name='ip',
            field=models.CharField(help_text='если принтер не сетевой, то поле заполнить значением: USB', max_length=25, validators=[django.core.validators.RegexValidator(regex='^(25[0-5]|2[0-4]\\d|[0-1]?\\d?\\d)(\\.(25[0-5]|2[0-4]\\d|[0-1]?\\d?\\d)){3}$|^USB$|^USB-TERM\\((25[0-5]|2[0-4]\\d|[0-1]?\\d?\\d)(\\.(25[0-5]|2[0-4]\\d|[0-1]?\\d?\\d)){3}\\)$|^\\-$')], verbose_name='IP'),
        ),
        migrations.AlterField(
            model_name='zip',
            name='shelf',
            field=models.CharField(help_text='<стеллаж>-<ярус> например: D-1', max_length=10, validators=[django.core.validators.RegexValidator(message='стеллаж - заглавная латинская буква, ярус - цифра', regex='^[A-Z]\\-[0-9]$')], verbose_name='№ полки'),
        ),
    ]
