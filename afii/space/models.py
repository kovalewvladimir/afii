from django.db import models


class Space(models.Model):
    """
    Площадка
    """
    name = models.CharField(max_length=50, unique=True, verbose_name='имя')
    description = models.TextField(blank=True, null=True, verbose_name='описание')

    class Meta:
        verbose_name = 'площадка'
        verbose_name_plural = 'площадка'

    def __str__(self):
        return self.name
