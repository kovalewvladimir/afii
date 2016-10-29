from django.db import models
from django.urls import reverse


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
