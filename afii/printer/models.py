from django.db import models
from space.models import Space


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
    ('DRAM', 'Драм-картридж'),
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


class BasePrinter(models.Model):
    """
    Базовый принтер
    """
    name = models.CharField(max_length=50, unique=True, verbose_name='Имя')
    type_printing = models.CharField(max_length=10, choices=PRINTING_TYPE, verbose_name='Тип принтера')
    type = models.CharField(max_length=10, choices=PRINTER_TYPE, verbose_name='Тип устройства')
    color = models.CharField(max_length=10, choices=CARTRIDGE_COLOR, verbose_name='Цвет')
    type_paper = models.CharField(max_length=50, choices=PAPER_TYPE, verbose_name='Формат бумаги')
    info_consumables = models.URLField(max_length=200, blank=True, null=True,
                                       verbose_name='Информация по расходникам')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return self.name


class BaseCartridge(models.Model):
    """
    Базовый картридж
    """
    name = models.CharField(max_length=50, unique=True, verbose_name='Имя')
    type = models.CharField(max_length=10, choices=CARTRIDGE_TYPE, verbose_name='Тип картриджа')
    color = models.CharField(max_length=10, choices=CARTRIDGE_COLOR,
                             blank=True, null=True, verbose_name='Цвет',
                             help_text='Заполнить поле только для \'тонер-картиржа\'',)
    recycling = models.BooleanField(verbose_name='Рециклинг',
                                    help_text='Заполнить поле только для "тонер-картиржа"')
    base_printers = models.ManyToManyField(BasePrinter, blank=True, related_name='base_cartridges',
                                           verbose_name='Базовый принтер')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return self.name


class BaseZip(models.Model):
    """
    Базовый ЗИП
    """
    name = models.CharField(max_length=50, unique=True, verbose_name='Имя')
    type = models.CharField(max_length=50, blank=True, null=True, verbose_name='Тип ЗИП')
    base_printers = models.ManyToManyField(BasePrinter, blank=True, related_name='base_zips')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return self.name


class Printer(models.Model):
    """
    Принетер
    """
    base_printer = models.ForeignKey(BasePrinter, related_name='printers',
                                     verbose_name='Базовый принтер')
    space = models.ForeignKey(Space, related_name='printers', verbose_name='Площадка')
    cabinet = models.CharField(max_length=50, verbose_name='№ кабинета')
    user = models.CharField(max_length=50, blank=True, null=True, verbose_name='Пользователь')
    login = models.CharField(max_length=50, blank=True, null=True, verbose_name='User')
    password = models.CharField(max_length=50, blank=True, null=True, verbose_name='Password')
    ip = models.CharField(max_length=15, verbose_name='IP',
                          help_text='Если принтер не сетевой, то поле заполнить значением: USB')
    sn = models.CharField(max_length=20, blank=True, null=True, verbose_name='Серийный номер')
    date = models.DateField(blank=True, null=True, verbose_name='Дата установки')
    description = models.TextField(blank=True, null=True, verbose_name='Примечание')
    image = models.ImageField(blank=True, null=True, upload_to='printers/')
    delete = models.BooleanField(default=False, verbose_name='Удален?')

    def __str__(self):
        return str("{}-{}-{}".format(self.space, self.cabinet, self.base_printer))


class Cartridge(models.Model):
    """
    Картридж
    """
    base_cartridge = models.ForeignKey(BaseCartridge, related_name='cartridges', verbose_name='Картридж')
    space = models.ForeignKey(Space, related_name='cartridges', verbose_name='Площадка')
    shelf = models.CharField(max_length=10, verbose_name='№ полки')
    count = models.PositiveIntegerField(verbose_name='Кол-во')
    min_count = models.PositiveIntegerField(verbose_name='Минимальное кол-во')
    count_recycling = models.PositiveIntegerField(blank=True, default=0, verbose_name='Кол-во в рециклинг')
    description = models.TextField(blank=True, null=True, verbose_name='Примечание')
    image = models.ImageField(blank=True, null=True, upload_to='cartridges/')
    delete = models.BooleanField(default=False, verbose_name='Удален?')

    def __str__(self):
        return str('{}-{}'.format(self.space, self.base_cartridge))


class Zip(models.Model):
    """
    ЗИП
    """
    base_zip = models.ForeignKey(BaseZip, related_name='zips', verbose_name='ЗИП')
    space = models.ForeignKey(Space, related_name='zips', verbose_name='Площадка')
    shelf = models.CharField(max_length=10, verbose_name='№ полки')
    count = models.PositiveIntegerField(verbose_name='Кол-во')
    min_count = models.PositiveIntegerField(verbose_name='Минимальное кол-во')
    description = models.TextField(blank=True, null=True, verbose_name='Примечание')
    image = models.ImageField(blank=True, null=True, upload_to='zips/')
    delete = models.BooleanField(default=False, verbose_name='Удален?')

    def __str__(self):
        return str('{}-{}').format(self.space, self.base_zip)
