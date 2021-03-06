# Generated by Django 2.2.1 on 2019-05-24 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printer', '0014_auto_20161118_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseprinter',
            name='type_paper',
            field=models.CharField(choices=[('1', 'A0, A1, A2, A3, A4'), ('2', 'A0, A1, A2, A3'), ('3', 'A0, A1, A2'), ('4', 'A0, A1'), ('5', 'A3, A4'), ('6', 'A0'), ('7', 'A1'), ('8', 'A2'), ('9', 'A3'), ('10', 'A4'), ('11', 'Иное')], max_length=50, verbose_name='формат бумаги'),
        ),
        migrations.AlterField(
            model_name='baseprinter',
            name='type_printing',
            field=models.CharField(choices=[('JET', 'Струйный'), ('LASER', 'Лазер'), ('SOLID', 'Твердочернильный'), ('THERMO', 'Термотрансферный')], max_length=10, verbose_name='технология печати'),
        ),
    ]
