from django.db import models
from space.models import Space


class Storage(models.Model):
    """
    Склад
    """
    class Meta:
        unique_together = ('name', 'space',)

    space = models.ForeignKey(Space, related_name='storage', verbose_name='площадка')
    name = models.CharField(max_length=50, verbose_name='имя')
    description = models.TextField(blank=True, null=True, verbose_name='описание')

    class Meta:
        verbose_name = 'склад'
        verbose_name_plural = 'склад'

    def __str__(self):
        return self.name
