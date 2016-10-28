from django.db import models


class Space(models.Model):
    """
    Площадка
    """
    name = models.CharField(max_length=50, unique=True, verbose_name='Имя')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return self.name
