# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-29 12:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('space', '0002_space'),
        ('printer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseCartridge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='имя')),
                ('type', models.CharField(choices=[('TONER', 'Тонер-картридж'), ('DRAM', 'Драм-картридж'), ('JET', 'Струйный-картридж')], max_length=10, verbose_name='тип картриджа')),
                ('color', models.CharField(blank=True, choices=[('BLACK', 'Черный'), ('COLOR', 'Цветной'), ('YELLOW', 'Желтый'), ('BLUE', 'Синий'), ('RED', 'Красный')], help_text="заполнить поле только для 'тонер-картиржа'", max_length=10, null=True, verbose_name='цвет')),
                ('recycling', models.BooleanField(help_text='заполнить поле только для "тонер-картиржа"', verbose_name='Рециклинг')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
            ],
            options={
                'verbose_name_plural': 'картриджи',
                'verbose_name': 'картридж',
            },
        ),
        migrations.CreateModel(
            name='BasePrinter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='имя')),
                ('type_printing', models.CharField(choices=[('JET', 'Струйный'), ('LASER', 'Лазер'), ('SOLID', 'Твердочернильный')], max_length=10, verbose_name='технология печати')),
                ('type', models.CharField(choices=[('PSC', 'Принтер, копир, сканер'), ('PRINTER', 'Принтер'), ('SCANNER', 'Сканер'), ('COPY', 'Копир'), ('PLOTTER', 'Плоттер')], max_length=10, verbose_name='тип устройства')),
                ('color', models.CharField(choices=[('BLACK', 'Черный'), ('COLOR', 'Цветной'), ('YELLOW', 'Желтый'), ('BLUE', 'Синий'), ('RED', 'Красный')], max_length=10, verbose_name='цвет')),
                ('type_paper', models.CharField(choices=[('1', 'A0, A1, A2, A3, A4'), ('2', 'A0, A1, A2, A3'), ('3', 'A0, A1, A2'), ('4', 'A0, A1'), ('5', 'A3, A4'), ('6', 'A0'), ('7', 'A1'), ('8', 'A2'), ('9', 'A3'), ('10', 'A4')], max_length=50, verbose_name='формат бумаги')),
                ('info_consumables', models.URLField(blank=True, null=True, verbose_name='информация по расходникам')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
            ],
            options={
                'verbose_name_plural': 'принтеры',
                'verbose_name': 'принтер',
            },
        ),
        migrations.CreateModel(
            name='BaseZip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='имя')),
                ('type', models.CharField(blank=True, max_length=50, null=True, verbose_name='тип ЗИП')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('base_printers', models.ManyToManyField(blank=True, related_name='base_zips', to='printer.BasePrinter', verbose_name='принтер')),
            ],
            options={
                'verbose_name_plural': 'запчасти для принтера',
                'verbose_name': 'запчасти для принтера',
            },
        ),
        migrations.CreateModel(
            name='Cartridge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shelf', models.CharField(max_length=10, verbose_name='№ полки')),
                ('count', models.PositiveIntegerField(verbose_name='кол-во')),
                ('min_count', models.PositiveIntegerField(verbose_name='минимальное кол-во')),
                ('count_recycling', models.PositiveIntegerField(blank=True, default=0, verbose_name='кол-во в рециклинг')),
                ('description', models.TextField(blank=True, null=True, verbose_name='примечание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='cartridges/')),
                ('is_active', models.BooleanField(default=True, verbose_name='используется')),
                ('base_cartridge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cartridges', to='printer.BaseCartridge', verbose_name='картридж')),
                ('space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cartridges', to='space.Space', verbose_name='площадка')),
            ],
            options={
                'verbose_name_plural': 'картриджи организации',
                'verbose_name': 'картридж организации',
            },
        ),
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cabinet', models.CharField(max_length=50, verbose_name='№ кабинета')),
                ('user', models.CharField(blank=True, max_length=50, null=True, verbose_name='пользователь')),
                ('login', models.CharField(blank=True, max_length=50, null=True, verbose_name='user')),
                ('password', models.CharField(blank=True, max_length=50, null=True, verbose_name='password')),
                ('ip', models.CharField(help_text='если принтер не сетевой, то поле заполнить значением: USB', max_length=15, verbose_name='IP')),
                ('sn', models.CharField(blank=True, max_length=20, null=True, verbose_name='серийный номер')),
                ('date', models.DateField(blank=True, null=True, verbose_name='дата установки')),
                ('description', models.TextField(blank=True, null=True, verbose_name='примечание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='printers/')),
                ('is_active', models.BooleanField(default=True, verbose_name='используется')),
                ('base_printer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='printers', to='printer.BasePrinter', verbose_name='принтер')),
                ('space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='printers', to='space.Space', verbose_name='площадка')),
            ],
            options={
                'verbose_name_plural': 'принтеры организации',
                'verbose_name': 'принтер организации',
            },
        ),
        migrations.CreateModel(
            name='Zip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shelf', models.CharField(max_length=10, verbose_name='№ полки')),
                ('count', models.PositiveIntegerField(verbose_name='Кол-во')),
                ('min_count', models.PositiveIntegerField(verbose_name='минимальное кол-во')),
                ('description', models.TextField(blank=True, null=True, verbose_name='примечание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='zips/')),
                ('is_active', models.BooleanField(default=True, verbose_name='используется')),
                ('base_zip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='zips', to='printer.BaseZip', verbose_name='ЗИП')),
                ('space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='zips', to='space.Space', verbose_name='площадка')),
            ],
            options={
                'verbose_name_plural': 'запчасти для принтера организации',
                'verbose_name': 'запчасти для принтера организации',
            },
        ),
        migrations.AddField(
            model_name='basecartridge',
            name='base_printers',
            field=models.ManyToManyField(blank=True, related_name='base_cartridges', to='printer.BasePrinter', verbose_name='принтер'),
        ),
    ]