from django.db import models
from django.urls import reverse

from inventory.table import Item
from space.models import Space
from printer import managers


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

    name = models.CharField(max_length=50, unique=True, verbose_name='имя')
    type_printing = models.CharField(max_length=10, choices=PRINTING_TYPE, verbose_name='технология печати')
    type = models.CharField(max_length=10, choices=PRINTER_TYPE, verbose_name='тип устройства')
    color = models.CharField(max_length=10, choices=CARTRIDGE_COLOR, verbose_name='цвет')
    type_paper = models.CharField(max_length=50, choices=PAPER_TYPE, verbose_name='формат бумаги')
    info_consumables = models.URLField(max_length=200, blank=True, null=True,
                                       verbose_name='информация по расходникам')
    description = models.TextField(blank=True, null=True, verbose_name='описание')

    class Meta:
        verbose_name = 'принтер'
        verbose_name_plural = 'принтеры'

    def __str__(self):
        return self.name


class BaseCartridge(models.Model):
    """
    Базовый картридж
    """
    name = models.CharField(max_length=50, unique=True, verbose_name='имя')
    type = models.CharField(max_length=10, choices=CARTRIDGE_TYPE, verbose_name='тип картриджа')
    color = models.CharField(max_length=10, choices=CARTRIDGE_COLOR,
                             blank=True, null=True, verbose_name='цвет',
                             help_text='заполнить поле только для \'тонер-картиржа\'',)
    recycling = models.BooleanField(verbose_name='Рециклинг',
                                    help_text='заполнить поле только для "тонер-картиржа"')
    base_printers = models.ManyToManyField(BasePrinter, blank=True, related_name='base_cartridges',
                                           verbose_name='принтер')
    description = models.TextField(blank=True, null=True, verbose_name='описание')

    class Meta:
        verbose_name = 'картридж'
        verbose_name_plural = 'картриджи'

    def __str__(self):
        return self.name


class BaseZip(models.Model):
    """
    Базовый ЗИП
    """
    name = models.CharField(max_length=50, unique=True, verbose_name='имя')
    type = models.CharField(max_length=50, blank=True, null=True, verbose_name='тип ЗИП')
    base_printers = models.ManyToManyField(BasePrinter, blank=True, related_name='base_zips',
                                           verbose_name='принтер')
    description = models.TextField(blank=True, null=True, verbose_name='описание')

    class Meta:
        verbose_name = 'запчасти для принтера'
        verbose_name_plural = 'запчасти для принтера'

    def __str__(self):
        return self.name


class Printer(models.Model):
    """
    Принетер
    """
    base_printer = models.ForeignKey(BasePrinter, related_name='printers',
                                     verbose_name='принтер')
    space = models.ForeignKey(Space, related_name='printers', verbose_name='площадка')
    cabinet = models.CharField(max_length=50, verbose_name='№ кабинета')
    user = models.CharField(max_length=50, blank=True, null=True, verbose_name='пользователь')
    login = models.CharField(max_length=50, blank=True, null=True, verbose_name='user')
    password = models.CharField(max_length=50, blank=True, null=True, verbose_name='password')
    ip = models.CharField(max_length=15, verbose_name='IP',
                          help_text='если принтер не сетевой, то поле заполнить значением: USB')
    sn = models.CharField(max_length=20, blank=True, null=True, verbose_name='серийный номер')
    date = models.DateField(blank=True, null=True, verbose_name='дата установки')
    description = models.TextField(blank=True, null=True, verbose_name='примечание')
    image = models.ImageField(blank=True, null=True, upload_to='printers/')
    is_active = models.BooleanField(default=True, verbose_name='используется')

    objects = managers.PrinterManager()

    class Meta:
        verbose_name = 'принтер организации'
        verbose_name_plural = 'принтеры организации'

    def get_items_toner_cartridge(self, space_id):
        items = list()
        items += [Item(c.base_cartridge.name, reverse('printer:cartridge', args=[c.pk]))
                  for bc in self.base_printer.base_cartridges.all()
                  if bc.type != 'DRAM'
                  for c in bc.cartridges.all()
                  if c.is_active and c.space.pk == space_id]
        return items

    def get_items_dram_cartridge(self, space_id):
        items = list()
        items += [Item(c.base_cartridge.name, reverse('printer:cartridge', args=[c.pk]))
                  for bc in self.base_printer.base_cartridges.all()
                  if bc.type == 'DRAM'
                  for c in bc.cartridges.all()
                  if c.is_active and c.space.pk == space_id]
        return items

    def __str__(self):
        return str("{}-{}-{}".format(self.space, self.cabinet, self.base_printer))


class Cartridge(models.Model):
    """
    Картридж
    """
    base_cartridge = models.ForeignKey(BaseCartridge, related_name='cartridges', verbose_name='картридж')
    space = models.ForeignKey(Space, related_name='cartridges', verbose_name='площадка')
    shelf = models.CharField(max_length=10, verbose_name='№ полки')
    count = models.PositiveIntegerField(verbose_name='кол-во')
    min_count = models.PositiveIntegerField(verbose_name='минимальное кол-во')
    count_recycling = models.PositiveIntegerField(blank=True, default=0, verbose_name='кол-во в рециклинг')
    description = models.TextField(blank=True, null=True, verbose_name='примечание')
    image = models.ImageField(blank=True, null=True, upload_to='cartridges/')
    is_active = models.BooleanField(default=True, verbose_name='используется')

    class Meta:
        verbose_name = 'картридж организации'
        verbose_name_plural = 'картриджи организации'

    def __str__(self):
        return str('{}-{}'.format(self.space, self.base_cartridge))


class Zip(models.Model):
    """
    ЗИП
    """
    base_zip = models.ForeignKey(BaseZip, related_name='zips', verbose_name='ЗИП')
    space = models.ForeignKey(Space, related_name='zips', verbose_name='площадка')
    shelf = models.CharField(max_length=10, verbose_name='№ полки')
    count = models.PositiveIntegerField(verbose_name='Кол-во')
    min_count = models.PositiveIntegerField(verbose_name='минимальное кол-во')
    description = models.TextField(blank=True, null=True, verbose_name='примечание')
    image = models.ImageField(blank=True, null=True, upload_to='zips/')
    is_active = models.BooleanField(default=True, verbose_name='используется')

    class Meta:
        verbose_name = 'запчасти для принтера организации'
        verbose_name_plural = 'запчасти для принтера организации'

    def __str__(self):
        return str('{}-{}').format(self.space, self.base_zip)
