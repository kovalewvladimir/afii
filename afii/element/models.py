from django.db import models

from printer.models import PAPER_TYPE
from space.models import Space
from element import managers

LAN_TYPE = (
    ('INTEGRATED', 'Встроенный'),
    ('EXTERNAL', 'Внешний (PCI)'),
)


class Paper(models.Model):
    """
    Бумага
    """

    class Meta:
        unique_together = ('name', 'space',)
        verbose_name = 'бумага'
        verbose_name_plural = 'бумага'

    name = models.CharField(max_length=50, verbose_name='имя')
    space = models.ForeignKey(Space, related_name='papers', verbose_name='площадка')
    type_paper = models.CharField(max_length=50, choices=PAPER_TYPE, verbose_name='формат бумаги')
    size = models.CharField(max_length=50, verbose_name='размеры', help_text='например: 841мм X 175м')
    count = models.PositiveIntegerField(verbose_name='кол-во')
    min_count = models.PositiveIntegerField(verbose_name='минимальное кол-во')
    description = models.TextField(blank=True, null=True, verbose_name='примечание')
    image = models.ImageField(blank=True, null=True, upload_to='papers/')
    is_active = models.BooleanField(default=True, verbose_name='используется')

    objects = managers.ElementManager()

    def __str__(self):
        return self.name


class Distribution(models.Model):
    """
    Дистрибутивы
    """

    class Meta:
        unique_together = ('name', 'space',)
        verbose_name = 'дистрибутив'
        verbose_name_plural = 'дистрибутивы'

    name = models.CharField(max_length=50, verbose_name='наименование')
    space = models.ForeignKey(Space, related_name='distributions', verbose_name='площадка')
    count = models.PositiveIntegerField(verbose_name='кол-во')
    image = models.ImageField(blank=True, null=True, upload_to='distributions/')
    is_active = models.BooleanField(default=True, verbose_name='используется')

    objects = managers.ElementManager()

    def __str__(self):
        return self.name


class Computer(models.Model):
    """
    Системные блоки
    """

    class Meta:
        verbose_name = 'системный блок'
        verbose_name_plural = 'системные блоки'

    space = models.ForeignKey(Space, related_name='computers', verbose_name='площадка')
    cpu = models.CharField(max_length=50, blank=True, null=True, verbose_name='процессор')
    motherboard = models.CharField(max_length=50, blank=True, null=True, verbose_name='материнская плата')
    ram = models.CharField(max_length=50, blank=True, null=True, verbose_name='оперативная память')
    gpu = models.CharField(max_length=50, blank=True, null=True, verbose_name='видеокарта')
    lan = models.CharField(max_length=20, blank=True, null=True, choices=LAN_TYPE, verbose_name='сетевой адаптер')
    power_supply = models.CharField(max_length=50, blank=True, null=True, verbose_name='блок питания')
    license_sticker = models.BooleanField(default=False, verbose_name='наклейка лицензии')
    hdd = models.CharField(max_length=50, blank=True, default='-', verbose_name='жесткий диск')
    os = models.CharField(max_length=50, blank=True, null=True, verbose_name='операционная система')
    description = models.TextField(blank=True, null=True, verbose_name='примечание')
    image = models.ImageField(blank=True, null=True, upload_to='computers/')
    is_active = models.BooleanField(default=True, verbose_name='используется')

    objects = managers.ElementManager()

    def __str__(self):
        return str(self.pk)
