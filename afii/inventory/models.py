from itertools import count

from django.db import models

IMAGE_UPLOAD_TO = 'media/'

PRINTING_TYPE = (
    ('JET', 'Струйный'),
    ('LASER', 'Лазер'),
    ('SOLID', 'Твердочернильный'),
)
PRINTER_TYPE = (
    ('PSC', 'Принтер, копир, сканер'),
    ('PRINTER', 'Принтер'),
    ('SCANNER', 'Сканер'),
    ('COPY', 'Копир'),
    ('PLOTTER', 'Плоттер'),
)
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
PAPER_TYPE = (
    ('1', 'A0, A1, A2, A3, A4'),
    ('2', 'A0, A1, A2, A3'),
    ('3', 'A0, A1, A2'),
    ('4', 'A0, A1'),
    ('5', 'A3, A4'),
    ('6', 'A0'),
    ('7', 'A1'),
    ('8', 'A2'),
    ('9', 'A3'),
    ('10', 'A4'),
)


class Space(models.Model):
    '''
    Площадка
    '''
    name = models.CharField(max_length=50, unique=True, verbose_name='Имя')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return str(self.name)

class Storage(models.Model):
    '''
    Склад
    '''
    space = models.ForeignKey(Space, related_name='storages', verbose_name='Площадка')
    name = models.CharField(max_length=50, unique=True, verbose_name='Имя')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return str('{0}-{1}').format(self.space, self.name)

class BasePrinter(models.Model):
    '''
    Базовый принтер
    '''
    # TODO: зипы
    name = models.CharField(max_length=50, unique=True, verbose_name='Имя')
    type_printing = models.CharField(max_length=10, choices=PRINTING_TYPE, verbose_name='Тип принтера')
    type = models.CharField(max_length=10, choices=PRINTER_TYPE, verbose_name='Тип устройства')
    color = models.CharField(max_length=10, choices=CARTRIDGE_COLOR, verbose_name='Цвет')
    papers = models.CharField(max_length=50, choices=PAPER_TYPE, verbose_name='Формат бумаги')
    info_consumables = models.URLField(max_length=200, blank=True, null=True, verbose_name='Информация по расходникам')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return str(self.name)

class BaseCartridge(models.Model):
    '''
    Базовый картридж
    '''
    name = models.CharField(max_length=50, unique=True, verbose_name='Имя')
    type = models.CharField(max_length=10, choices=CARTRIDGE_TYPE, verbose_name='Тип картриджа')
    color = models.CharField(max_length=10, choices=CARTRIDGE_COLOR, blank=True, null=True, verbose_name='Цвет')
    recycling = models.BooleanField(verbose_name='Рециклинг')
    base_printer = models.ManyToManyField(BasePrinter, blank=True, related_name='base_cartridges')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return str(self.name)

class Printer(models.Model):
    '''
    Принетер
    '''
    base_printer = models.ForeignKey(BasePrinter, related_name='printers')
    space = models.ForeignKey(Space, related_name='printers', verbose_name='Площадка')
    cabinet = models.CharField(max_length=50, verbose_name='№ кабинета')
    login = models.CharField(max_length=50, blank=True, null=True, verbose_name='User')
    password = models.CharField(max_length=50, blank=True, null=True, verbose_name='Password')
    ip = models.CharField(max_length=15, verbose_name='IP')
    sn = models.CharField(max_length=20,blank=True, null=True, verbose_name='Серийный номер')
    date = models.DateField(blank=True, null=True, verbose_name='Дата установки')
    description = models.TextField(blank=True, null=True, verbose_name='Примечание')
    image = models.ImageField(upload_to=IMAGE_UPLOAD_TO)

    def get_cartridges(self):
        return [c for bc in self.base_printer.base_cartridges.all() for c in bc.cartridges.select_related().all()]

    def __str__(self):
        return str("{}-{}-{}".format(self.space, self.cabinet, self.base_printer))

class Cartridge(models.Model):
    '''
    Картридж
    '''
    base_cartridge = models.ForeignKey(BaseCartridge, related_name='cartridges', verbose_name='Картридж')
    storage = models.ForeignKey(Storage, related_name='cartridges')
    shelf = models.CharField(max_length=10, verbose_name='№ полки')
    count = models.PositiveIntegerField(verbose_name='Кол-во')
    count_recycling = models.PositiveIntegerField(blank=True, null=True, verbose_name='Кол-во в рециклинг')
    image = models.ImageField(upload_to=IMAGE_UPLOAD_TO)

    def __str__(self):
        return str('{}-{}'.format(self.storage, self.base_cartridge))


# TODO: у ключючей on_delete















