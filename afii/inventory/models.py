from django.db import models

class Space(models.Model):
    '''
    Площадка
    '''
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return str(self.name)

class Storage(models.Model):
    '''
    Склад
    '''
    space = models.ForeignKey(Space, verbose_name='Площадка')
    name = models.CharField(max_length=50, verbose_name='Имя')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return str('{0} - {1}').format(self.space, self.name)

class BaseCartridge(models.Model):
    '''
    Базовый картридж
    '''
    CARTRIDGE_TYPE = (
        ('TONER', 'Тонер-картридж'),
        ('DRAMM', 'Драм-картридж'),
        ('JET', 'Струйный-картридж'),
    )
    CARTRIDGE_COLOR = (
        ('BLACK', 'Черный'),
        ('COLOR', 'Цветной'),
        ('YELLOW', 'Желтый'),
        ('BLUE', 'Синий'),
        ('RED', 'Красный'),
    )
    name = models.CharField(max_length=50, unique=True, verbose_name='Имя')
    type = models.CharField(max_length=10, choices=CARTRIDGE_TYPE, verbose_name='Тип картриджа')
    color = models.CharField(max_length=10, choices=CARTRIDGE_COLOR, blank=True, null=True, verbose_name='Цвет')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return str(self.name)


class BasePrinter(models.Model):
    '''
    Базовый принтер
    '''
    PRINTER_TYPE_PRINTING = (
        ('JET', 'Струйный'),
        ('LASER', 'Лазер'),
        ('SOLID', 'Твердочернильный'),
    )
    PRINTER_TYPE = (
        ('', 'Принтер, копир, сканер'),
        ('', 'Принтер'),
        ('', 'Сканер'),
        ('', 'Копир'),
        ('', 'Плоттер'),
    )
    CARTRIDGE_COLOR = (
        ('BLACK', 'Черный'),
        ('COLOR', 'Цветной'),
    )

    name = models.CharField(max_length=50, unique=True, verbose_name='Имя')
    type_printing = models.CharField(max_length=10, choices=PRINTER_TYPE_PRINTING, verbose_name='Тип принтера')
    type = models.CharField(max_length=10, choices=PRINTER_TYPE, verbose_name='Тип устройства')
    color = models.CharField(max_length=10, choices=CARTRIDGE_COLOR, verbose_name='Цвет')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    def __str__(self):
        return str(self.name)