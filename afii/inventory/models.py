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

LAN_TYPE = (
    ('INTEGRATED', 'Встроенная '),
    ('EXTERNAL', 'Внешняя (PCI)'),
)


class Space(models.Model):
    """
    Площадка
    """
    name = models.CharField(max_length=50, unique=True, verbose_name='Имя')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return str(self.name)


class Storage(models.Model):
    """
    Склад
    """
    space = models.ForeignKey(Space, related_name='storages', verbose_name='Площадка')
    name = models.CharField(max_length=50, unique=True, verbose_name='Имя')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return str('{0}-{1}').format(self.space, self.name)


class BasePrinter(models.Model):
    """
    Базовый принтер
    """
    name = models.CharField(max_length=50, unique=True, verbose_name='Имя')
    type_printing = models.CharField(max_length=10, choices=PRINTING_TYPE, verbose_name='Тип принтера')
    type = models.CharField(max_length=10, choices=PRINTER_TYPE, verbose_name='Тип устройства')
    color = models.CharField(max_length=10, choices=CARTRIDGE_COLOR, verbose_name='Цвет')
    type_paper = models.CharField(max_length=50, choices=PAPER_TYPE, verbose_name='Формат бумаги')
    info_consumables = models.URLField(max_length=200, blank=True, null=True, verbose_name='Информация по расходникам')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return str(str('{}-{}').format(self.pk, self.name))


class BaseCartridge(models.Model):
    """
    Базовый картридж
    """
    name = models.CharField(max_length=50, unique=True, verbose_name='Имя')
    type = models.CharField(max_length=10, choices=CARTRIDGE_TYPE, verbose_name='Тип картриджа')
    color = models.CharField(max_length=10, choices=CARTRIDGE_COLOR, blank=True, null=True, verbose_name='Цвет', help_text='Заполнить поле только для "тонер-картиржа"')
    recycling = models.BooleanField(verbose_name='Рециклинг', help_text='Заполнить поле только для "тонер-картиржа"')
    base_printers = models.ManyToManyField(BasePrinter, blank=True, related_name='base_cartridges')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return str(self.name)


class BaseZip(models.Model):
    """
    Базовый ЗИП
    """
    name = models.CharField(max_length=50, unique=True, verbose_name='Имя')
    type = models.CharField(max_length=50, blank=True, null=True, verbose_name='Тип ЗИП')
    base_printers = models.ManyToManyField(BasePrinter, blank=True, related_name='base_zips')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return str(self.name)


class Printer(models.Model):
    """
    Принетер
    """
    base_printer = models.ForeignKey(BasePrinter, related_name='printers')
    space = models.ForeignKey(Space, related_name='printers', verbose_name='Площадка')
    cabinet = models.CharField(max_length=50, verbose_name='№ кабинета')
    user = models.CharField(max_length=50, blank=True, null=True, verbose_name='Пользователь')
    login = models.CharField(max_length=50, blank=True, null=True, verbose_name='User')
    password = models.CharField(max_length=50, blank=True, null=True, verbose_name='Password')
    ip = models.CharField(max_length=15, verbose_name='IP')
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
    count_recycling = models.PositiveIntegerField(blank=True, null=True, verbose_name='Кол-во в рециклинг')
    description = models.TextField(blank=True, null=True, verbose_name='Примечание')
    image = models.ImageField(blank=True, null=True, upload_to='cartridges/')
    delete = models.BooleanField(default=False, verbose_name='Удален?')

    def __str__(self):
        return str('{}-{}'.format(self.space, self.base_cartridge))


class Zip(models.Model):
    """
    ЗИП
    """
    base_zips = models.ForeignKey(BaseZip, related_name='zips', verbose_name='ЗИП')
    space = models.ForeignKey(Space, related_name='zips', verbose_name='Площадка')
    shelf = models.CharField(max_length=10, verbose_name='№ полки')
    count = models.PositiveIntegerField(verbose_name='Кол-во')
    description = models.TextField(blank=True, null=True, verbose_name='Примечание')
    image = models.ImageField(blank=True, null=True, upload_to='zips/')
    delete = models.BooleanField(default=False, verbose_name='Удален?')

    def __str__(self):
        return str('{}-{}').format(self.space, self.base_zips)


class Paper(models.Model):
    """
    Бумага
    """
    name = models.CharField(max_length=50, unique=True, verbose_name='Имя')
    space = models.ForeignKey(Space, related_name='papers', verbose_name='Площадка')
    type_paper = models.CharField(max_length=50, choices=PAPER_TYPE, verbose_name='Формат бумаги')
    size = models.CharField(max_length=50, verbose_name='Размеры', help_text='Например: 841мм X 175м')
    count = models.PositiveIntegerField(verbose_name='Кол-во')
    min_count = models.PositiveIntegerField(verbose_name='Минимальное кол-во')
    description = models.TextField(blank=True, null=True, verbose_name='Примечание')
    image = models.ImageField(blank=True, null=True, upload_to='papers/')
    delete = models.BooleanField(default=False, verbose_name='Удален?')

    def __str__(self):
        return str('{}-{}').format(self.space, self.name)


class Distribution(models.Model):
    """
    Дистрибутивы
    """
    name = models.CharField(max_length=50, unique=True, verbose_name='Наименование')
    space = models.ForeignKey(Space, related_name='distributions', verbose_name='Площадка')
    count = models.PositiveIntegerField(verbose_name='Кол-во')
    image = models.ImageField(blank=True, null=True, upload_to='distributions/')
    delete = models.BooleanField(default=False, verbose_name='Удален?')

    def __str__(self):
        return str('{}-{}').format(self.space, self.name)


class Computer(models.Model):
    """
    Системные блоки
    """
    space = models.ForeignKey(Space, related_name='computers', verbose_name='Площадка')
    cpu = models.CharField(max_length=50, blank=True, null=True, verbose_name='Процессор')
    motherboard = models.CharField(max_length=50, blank=True, null=True, verbose_name='Материнская плата')
    ram = models.CharField(max_length=50, blank=True, null=True, verbose_name='Оперативная память')
    gpu = models.CharField(max_length=50, blank=True, null=True, verbose_name='Видеокарта')
    lan = models.CharField(max_length=20, blank=True, null=True,choices=LAN_TYPE, verbose_name='Сетевой адаптер')
    hdd = models.CharField(max_length=50, blank=True, default='-', verbose_name='Жесткий диск')
    os = models.CharField(max_length=50, blank=True, null=True, verbose_name='Операционная система')
    description = models.TextField(blank=True, null=True, verbose_name='Примечание')
    image = models.ImageField(blank=True, null=True, upload_to='computers/')
    delete = models.BooleanField(default=False, verbose_name='Удален?')

    def __str__(self):
        return str('{}-{}').format(self.space, self.cpu)


class Category(models.Model):
    """
    Категория
    """
    storage = models.ForeignKey(Storage, related_name='categories')
    name = models.CharField(max_length=50, unique=True, verbose_name='Имя')
    is_base = models.BooleanField(default=False, verbose_name='Вложенная категория?')
    base_categoty = models.ForeignKey('self', blank=True, null=True, limit_choices_to={'is_base': False})

    def __str__(self):
        return str('{}-{}').format(self.storage, self.name)






# TODO: у ключючей on_delete
