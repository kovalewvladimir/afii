from django.db import models


class InventoryApp(models.Model):
    """
    Приложения inventory
    """
    name = models.CharField(max_length=50, unique=True, verbose_name='имя')
    verbose_name = models.CharField(max_length=50, verbose_name='полное имя')
    description = models.TextField(blank=True, null=True, verbose_name='описание')

    class Meta:
        verbose_name = 'приложение inventory'
        verbose_name_plural = 'приложения inventory'

    def __str__(self):
        return self.name
