# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-25 11:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('space', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseCartridge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Имя')),
                ('type', models.CharField(choices=[('TONER', 'Тонер-картридж'), ('DRAM', 'Драм-картридж'), ('JET', 'Струйный-картридж')], max_length=10, verbose_name='Тип картриджа')),
                ('color', models.CharField(blank=True, choices=[('BLACK', 'Черный'), ('COLOR', 'Цветной'), ('YELLOW', 'Желтый'), ('BLUE', 'Синий'), ('RED', 'Красный')], help_text="Заполнить поле только для 'тонер-картиржа'", max_length=10, null=True, verbose_name='Цвет')),
                ('recycling', models.BooleanField(help_text='Заполнить поле только для "тонер-картиржа"', verbose_name='Рециклинг')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='BasePrinter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Имя')),
                ('type_printing', models.CharField(choices=[('JET', 'Струйный'), ('LASER', 'Лазер'), ('SOLID', 'Твердочернильный')], max_length=10, verbose_name='Тип принтера')),
                ('type', models.CharField(choices=[('PSC', 'Принтер, копир, сканер'), ('PRINTER', 'Принтер'), ('SCANNER', 'Сканер'), ('COPY', 'Копир'), ('PLOTTER', 'Плоттер')], max_length=10, verbose_name='Тип устройства')),
                ('color', models.CharField(choices=[('BLACK', 'Черный'), ('COLOR', 'Цветной'), ('YELLOW', 'Желтый'), ('BLUE', 'Синий'), ('RED', 'Красный')], max_length=10, verbose_name='Цвет')),
                ('type_paper', models.CharField(choices=[('1', 'A0, A1, A2, A3, A4'), ('2', 'A0, A1, A2, A3'), ('3', 'A0, A1, A2'), ('4', 'A0, A1'), ('5', 'A3, A4'), ('6', 'A0'), ('7', 'A1'), ('8', 'A2'), ('9', 'A3'), ('10', 'A4')], max_length=50, verbose_name='Формат бумаги')),
                ('info_consumables', models.URLField(blank=True, null=True, verbose_name='Информация по расходникам')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='BaseZip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Имя')),
                ('type', models.CharField(blank=True, max_length=50, null=True, verbose_name='Тип ЗИП')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('base_printers', models.ManyToManyField(blank=True, related_name='base_zips', to='printer.BasePrinter')),
            ],
        ),
        migrations.CreateModel(
            name='Cartridge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shelf', models.CharField(max_length=10, verbose_name='№ полки')),
                ('count', models.PositiveIntegerField(verbose_name='Кол-во')),
                ('min_count', models.PositiveIntegerField(verbose_name='Минимальное кол-во')),
                ('count_recycling', models.PositiveIntegerField(blank=True, default=0, verbose_name='Кол-во в рециклинг')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Примечание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='cartridges/')),
                ('delete', models.BooleanField(default=False, verbose_name='Удален?')),
                ('base_cartridge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cartridges', to='printer.BaseCartridge', verbose_name='Картридж')),
                ('space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cartridges', to='space.Space', verbose_name='Площадка')),
            ],
        ),
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cabinet', models.CharField(max_length=50, verbose_name='№ кабинета')),
                ('user', models.CharField(blank=True, max_length=50, null=True, verbose_name='Пользователь')),
                ('login', models.CharField(blank=True, max_length=50, null=True, verbose_name='User')),
                ('password', models.CharField(blank=True, max_length=50, null=True, verbose_name='Password')),
                ('ip', models.CharField(help_text='Если принтер не сетевой, то поле заполнить значением: USB', max_length=15, verbose_name='IP')),
                ('sn', models.CharField(blank=True, max_length=20, null=True, verbose_name='Серийный номер')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Дата установки')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Примечание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='printers/')),
                ('delete', models.BooleanField(default=False, verbose_name='Удален?')),
                ('base_printer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='printers', to='printer.BasePrinter')),
                ('space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='printers', to='space.Space', verbose_name='Площадка')),
            ],
        ),
        migrations.CreateModel(
            name='Zip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shelf', models.CharField(max_length=10, verbose_name='№ полки')),
                ('count', models.PositiveIntegerField(verbose_name='Кол-во')),
                ('min_count', models.PositiveIntegerField(verbose_name='Минимальное кол-во')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Примечание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='zips/')),
                ('delete', models.BooleanField(default=False, verbose_name='Удален?')),
                ('base_zip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='zips', to='printer.BaseZip', verbose_name='ЗИП')),
                ('space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='zips', to='space.Space', verbose_name='Площадка')),
            ],
        ),
        migrations.AddField(
            model_name='basecartridge',
            name='base_printers',
            field=models.ManyToManyField(blank=True, related_name='base_cartridges', to='printer.BasePrinter'),
        ),
    ]
