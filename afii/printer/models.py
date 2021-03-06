from django.core.validators import RegexValidator, URLValidator
from django.db import models
from django.urls import reverse
from datetime import date

from inventory.models import BaseModel, HELP_TEXT_SHELF, VALIDATOR_SHELF
from inventory.table import Item, Table
from space.models import Space
from printer.managers import PrinterManager, CartridgeManager, ZipManager

PRINTING_TYPE = (
    ('JET', 'Струйный'),
    ('LASER', 'Лазер'),
    ('SOLID', 'Твердочернильный'),
    ('THERMO', 'Термотрансферный'),
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
    ('11', 'Иное'),
)


class BasePrinter(BaseModel):
    """
    Базовый принтер
    """

    class Meta:
        verbose_name = 'принтер'
        verbose_name_plural = 'принтеры'

    name = models.CharField(max_length=50, unique=True, verbose_name='имя')
    type_printing = models.CharField(max_length=10, choices=PRINTING_TYPE, verbose_name='технология печати')
    type = models.CharField(max_length=10, choices=PRINTER_TYPE, verbose_name='тип устройства')
    color = models.CharField(max_length=10, choices=CARTRIDGE_COLOR, verbose_name='цвет')
    type_paper = models.CharField(max_length=50, choices=PAPER_TYPE, verbose_name='формат бумаги')
    info_consumables = models.CharField(max_length=200, blank=True, null=True,
                                        verbose_name='информация по расходникам')
    description = models.TextField(blank=True, null=True, verbose_name='описание')

    def __str__(self):
        return self.name


class BaseCartridge(BaseModel):
    """
    Базовый картридж
    """

    class Meta:
        verbose_name = 'картридж'
        verbose_name_plural = 'картриджи'

    name = models.CharField(max_length=50, unique=True, verbose_name='имя')
    type = models.CharField(max_length=10, choices=CARTRIDGE_TYPE, verbose_name='тип картриджа')
    color = models.CharField(max_length=10, choices=CARTRIDGE_COLOR,
                             blank=True, null=True, verbose_name='цвет',
                             help_text='заполнить поле только для \'тонер-картиржа\'', )
    recycling = models.BooleanField(default=False, verbose_name='Рециклинг',
                                    help_text='заполнить поле только для "тонер-картиржа"')
    base_printers = models.ManyToManyField(BasePrinter, blank=True, related_name='base_cartridges',
                                           verbose_name='принтер')
    description = models.TextField(blank=True, null=True, verbose_name='описание')

    def __str__(self):
        return self.name


class BaseZip(BaseModel):
    """
    Базовый ЗИП
    """

    class Meta:
        verbose_name = 'запчасти для принтера'
        verbose_name_plural = 'запчасти для принтера'

    name = models.CharField(max_length=50, unique=True, verbose_name='имя')
    type = models.CharField(max_length=50, blank=True, null=True, verbose_name='тип ЗИП')
    base_printers = models.ManyToManyField(BasePrinter, blank=True, related_name='base_zips',
                                           verbose_name='принтер')
    description = models.TextField(blank=True, null=True, verbose_name='описание')

    def __str__(self):
        return self.name


class Printer(BaseModel):
    """
    Принетер
    """

    class Meta:
        verbose_name = 'принтер организации'
        verbose_name_plural = 'принтеры организации'

    base_printer = models.ForeignKey(BasePrinter, related_name='printers',
                                     verbose_name='принтер', on_delete=models.CASCADE)
    space = models.ForeignKey(Space, related_name='printers', verbose_name='площадка',
                              on_delete=models.CASCADE)
    cabinet = models.CharField(max_length=50, verbose_name='№ кабинета')
    user = models.CharField(max_length=50, blank=True, null=True, verbose_name='пользователь')
    login = models.CharField(max_length=50, blank=True, null=True, verbose_name='user')
    password = models.CharField(max_length=50, blank=True, null=True, verbose_name='password')
    ip = models.CharField(max_length=25, verbose_name='IP',
                          help_text='если принтер не сетевой, то поле заполнить значением: USB или USB-TERM(<IP>)',
                          validators=[
                              RegexValidator(
                                  regex=r'^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$|'
                                        r'^USB$|'
                                        r'^USB-TERM'
                                        r'\((25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}\)$|'
                                        r'^\-$')
                          ])
    sn = models.CharField(max_length=20, blank=True, null=True, verbose_name='серийный номер')
    service = models.CharField(max_length=50, blank=True, null=True, default='Нет', verbose_name='обслуживание')
    date = models.DateField(default=date.today, verbose_name='дата установки')
    description = models.TextField(blank=True, null=True, verbose_name='примечание')
    image = models.ImageField(blank=True, null=True, upload_to='printers/')
    is_active = models.BooleanField(default=True, verbose_name='используется')

    objects = PrinterManager()

    def get_table_cartridges(self):
        """
        Получить таблицу с картриджами
        :return: таблица с картриджами
        """
        table_cartridges = {
            'toner': Table(),
            'dram': Table(),
        }
        for bc in self.base_printer.base_cartridges.all():
            tc = bc.cartridges.get_table(self.space.pk)
            table_cartridges['toner'] += tc['toner']
            table_cartridges['dram'] += tc['dram']
        if len(table_cartridges['toner'].rows) == 0:
            table_cartridges['toner'] = None
        if len(table_cartridges['dram'].rows) == 0:
            table_cartridges['dram'] = None
        return table_cartridges

    def get_table_zip(self):
        """
        Получить таблицу с ЗИПами
        :return: таблица с ЗИПами
        """
        table = Table()
        for z in self.base_printer.base_zips.all():
            table += z.zips.get_table(self.space.pk)
        if len(table.rows) == 0:
            table = None
        return table

    def get_items_cartridge(self, type_cartridge):
        """
        Получить список картриджей
        :param type_cartridge: тип картриджа
        :return: список картриджей
        """
        items = list()
        space_id = self.space.pk
        if type_cartridge == 'TONER':
            is_type = lambda t: t != 'DRAM'
        elif type_cartridge == 'DRAM':
            is_type = lambda t: t == 'DRAM'
        else:
            return None
        items += [Item(c, c.get_absolute_url())
                  for bc in self.base_printer.base_cartridges.all()
                  if is_type(bc.type)
                  for c in bc.cartridges.all()
                  if c.is_active and c.space.pk == space_id]
        return items

    def __str__(self):
        return str(self.base_printer)


class Cartridge(BaseModel):
    """
    Картридж
    """

    class Meta:
        unique_together = ('base_cartridge', 'space')
        verbose_name = 'картридж организации'
        verbose_name_plural = 'картриджи организации'

    base_cartridge = models.ForeignKey(BaseCartridge, related_name='cartridges', verbose_name='картридж',
                                       on_delete=models.CASCADE)
    space = models.ForeignKey(Space, related_name='cartridges', verbose_name='площадка',
                              on_delete=models.CASCADE)
    shelf = models.CharField(max_length=10, verbose_name='№ полки',
                             help_text=HELP_TEXT_SHELF, validators=[VALIDATOR_SHELF])
    count = models.PositiveIntegerField(verbose_name='кол-во')
    min_count = models.PositiveIntegerField(verbose_name='минимальное кол-во')
    count_recycling = models.PositiveIntegerField(blank=True, default=0, verbose_name='кол-во в рециклинг')
    count_in_recycling = models.PositiveIntegerField(blank=True, default=0, verbose_name='кол-во в рециклинге')
    description = models.TextField(blank=True, null=True, verbose_name='примечание')
    image = models.ImageField(blank=True, null=True, upload_to='cartridges/')
    is_active = models.BooleanField(default=True, verbose_name='используется')

    objects = CartridgeManager()

    def get_table_printer(self):
        """
        Получить таблицу с принтерами
        :return: таблица с принтерами
        """
        table = Table()
        for bp in self.base_cartridge.base_printers.all():
            table += bp.printers.get_table(self.space.pk)
        return table

    def get_item_printer(self):
        """
        Получить список принтеров
        :return: список принтеров
        """
        items = list()
        space_id = self.space.pk
        items += [Item(p, p.get_absolute_url())
                  for bp in self.base_cartridge.base_printers.all()
                  for p in bp.printers.all()
                  if p.is_active and p.space.pk == space_id]
        return items

    def __str__(self):
        return str(self.base_cartridge)


class Zip(BaseModel):
    """
    ЗИП
    """

    class Meta:
        unique_together = ('base_zip', 'space')
        verbose_name = 'запчасти для принтера организации'
        verbose_name_plural = 'запчасти для принтера организации'

    base_zip = models.ForeignKey(BaseZip, related_name='zips', verbose_name='ЗИП', on_delete=models.CASCADE)
    space = models.ForeignKey(Space, related_name='zips', verbose_name='площадка', on_delete=models.CASCADE)
    shelf = models.CharField(max_length=10, verbose_name='№ полки',
                             help_text=HELP_TEXT_SHELF, validators=[VALIDATOR_SHELF])
    count = models.PositiveIntegerField(verbose_name='Кол-во')
    min_count = models.PositiveIntegerField(verbose_name='минимальное кол-во')
    description = models.TextField(blank=True, null=True, verbose_name='примечание')
    image = models.ImageField(blank=True, null=True, upload_to='zips/')
    is_active = models.BooleanField(default=True, verbose_name='используется')

    objects = ZipManager()

    def get_table_printer(self):
        """
        Получить таблицу с принтерами
        :return: таблица с принтерами
        """
        table = Table()
        for bp in self.base_zip.base_printers.all():
            table += bp.printers.get_table(self.space.pk)
        return table

    def get_item_printer(self):
        """
        Получить список принтеров
        :return: список принтеров
        """
        items = list()
        space_id = self.space.pk
        items += [Item(p, p.get_absolute_url())
                  for bp in self.base_zip.base_printers.all()
                  for p in bp.printers.all()
                  if p.is_active and p.space.pk == space_id]
        return items

    def __str__(self):
        return str(self.base_zip)
