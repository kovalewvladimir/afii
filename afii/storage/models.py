from django.db import models
from space.models import Space


class Storage(models.Model):
    """
    Склад
    """
    class Meta:
        unique_together = ('name', 'space',)

    space = models.ForeignKey(Space, related_name='storage', verbose_name='Площадка')
    name = models.CharField(max_length=50, verbose_name='Имя')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return self.name
