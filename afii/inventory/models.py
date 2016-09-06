from django.db import models

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


class Space(models.Model):
    '''
    Площадка
    '''
    name = models.CharField(max_length=50, verbose_name='Имя')
    description = models.TextField( blank=True, null=True, verbose_name='Описание')

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
    name = models.CharField(max_length=50, unique=True, verbose_name='Имя')
    type = models.CharField(max_length=10, choices=CARTRIDGE_TYPE, verbose_name='Тип картриджа')
    color = models.CharField(max_length=10, choices=CARTRIDGE_COLOR, blank=True, null=True, verbose_name='Цвет')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return str(self.name)


class PaperSize(models.Model):
    '''
    Формат бумаги
    '''
    size = models.CharField(max_length=50, unique=True, verbose_name='Формат бумаги')

    def __str__(self):
        return str(self.size)

class BasePrinter(models.Model):
    '''
    Базовый принтер
    '''
    # TODO: зипы
    name = models.CharField(max_length=50, unique=True, verbose_name='Имя')
    type_printing = models.CharField(max_length=10, choices=PRINTING_TYPE, verbose_name='Тип принтера')
    type = models.CharField(max_length=10, choices=PRINTER_TYPE, verbose_name='Тип устройства')
    color = models.CharField(max_length=10, choices=CARTRIDGE_COLOR, verbose_name='Цвет')
    papers = models.ManyToManyField(PaperSize, verbose_name='Формат бумаги')
    base_cartridge = models.ManyToManyField(BaseCartridge, verbose_name='Картридж')
    info_consumables = models.URLField(max_length=200, blank=True, null=True, verbose_name='Информация по расходникам')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return str(self.name)

class Printer(models.Model):
    '''
    Принетер
    '''
    name = models.CharField(max_length=50, unique=True, verbose_name='Имя')
    user = models.CharField(max_length=50, verbose_name='Пользователь')
    ip = models.CharField(max_length=15, verbose_name='IP')
    base_printer = models.ForeignKey(BasePrinter)

    def __str__(self):
        return str(self.name)

class Cartridge(models.Model):
    '''
    Картридж
    '''
    name = models.CharField(max_length=50, unique=True, verbose_name='Имя')
    base_cartridge = models.ForeignKey(BaseCartridge, verbose_name='Картридж')

    def __str__(self):
        return str(self.name)

















