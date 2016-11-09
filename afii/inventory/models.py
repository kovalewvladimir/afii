from django.db import models
from django.urls import reverse

from element.managers import ElementManager
from inventory.managers import TableManager


class BaseModel(models.Model):
    class Meta:
        abstract = True

    def get_absolute_url(self):
        return reverse('%s:%s' % (self._meta.app_label, self._meta.model_name), args=(self.pk,))

    def get_admin_change_edit(self):
        return reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=(self.pk,))

    def get_verbose_name(self):
        return self._meta.verbose_name

    def get_field(self, field):
        name = self._meta.get_field(field).verbose_name.capitalize()
        if name == 'Id':
            name = '№'
        return name
    

class InventoryApp(models.Model):
    """
    Приложения inventory
    """
    app_name = models.CharField(max_length=50, unique=True, verbose_name='имя')
    verbose_name = models.CharField(max_length=50, verbose_name='полное имя')
    view_name_url = models.CharField(max_length=50, verbose_name='view_name_url')
    description = models.TextField(blank=True, null=True, verbose_name='описание')

    class Meta:
        verbose_name = 'приложение inventory'
        verbose_name_plural = 'приложения inventory'

    def get_url(self):
        return self.view_name_url

    def __str__(self):
        return self.verbose_name
