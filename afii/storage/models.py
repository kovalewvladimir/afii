from django.db import models

from space.models import Space
from storage.managers import CategoryManager, ItemStorageManager
from inventory.models import BaseModel, HELP_TEXT_SHELF, VALIDATOR_SHELF


class Storage(models.Model):
    """
    Склад
    """

    class Meta:
        unique_together = ('name', 'space',)
        verbose_name = 'склад'
        verbose_name_plural = 'склад'

    space = models.ForeignKey(Space, related_name='storage', verbose_name='площадка')
    name = models.CharField(max_length=50, verbose_name='имя')
    description = models.TextField(blank=True, null=True, verbose_name='описание')

    def __str__(self):
        return '%s-%s' % (self.space, self.name)


class Category(BaseModel):
    """
    Категория
    """

    class Meta:
        unique_together = ('name', 'storage', 'base_category')
        verbose_name = 'категории'
        verbose_name_plural = 'категория'

    storage = models.ForeignKey(Storage, related_name='categories', verbose_name='склад')
    name = models.CharField(max_length=50, verbose_name='имя')
    is_base = models.BooleanField(default=False, verbose_name='базовая категория?')
    base_category = models.ForeignKey('self', blank=True, null=True, related_name='categories',
                                      limit_choices_to={'is_base': True}, verbose_name='базовая категория')

    objects = CategoryManager()

    def __str__(self):
        if self.base_category is None:
            return '%s-%s' % (self.storage, self.name)
        else:
            return '%s-%s-%s' % (self.storage, self.base_category.name, self.name)


class ItemStorage(BaseModel):
    """
    Единица складского учета
    """

    class Meta:
        unique_together = ('name', 'category',)
        verbose_name = 'единица складского учета'
        verbose_name_plural = 'единица складского учета'

    category = models.ForeignKey(Category, related_name='items', limit_choices_to={'is_base': False},
                                 verbose_name='категория')
    name = models.CharField(max_length=50, verbose_name='наименование')
    count = models.PositiveIntegerField(verbose_name='кол-во')
    shelf = models.CharField(max_length=10, verbose_name='№ полки',
                             help_text=HELP_TEXT_SHELF, validators=[VALIDATOR_SHELF])
    is_active = models.BooleanField(default=True, verbose_name='используется')
    image = models.ImageField(blank=True, null=True, upload_to='item_storage/')
    description = models.TextField(blank=True, null=True, verbose_name='примечание')

    objects = ItemStorageManager()

    def __str__(self):
        return self.name
