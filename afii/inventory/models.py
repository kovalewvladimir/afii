from django.db import models

class Space(models.Model):
    '''
    Площадка
    '''

    class Meta():
        db_table = 'space'

    space_name = models.CharField(max_length=50, blank=True, null=True)
    space_description = models.TextField()

class Storage(models.Model):
    '''
    Склад
    '''
    class Meta():
        db_table = 'storage'

    storage_space = models.ForeignKey(Space)
    storage_name = models.CharField(max_length=50, blank=True, null=True)
    storage_description = models.TextField()

class TypeCartridge(models.Model):
    '''

    '''
    class Meta():
        db_table = 'typeCartridge'

class BaseCartridge(models.Model):
    '''

    '''

class BasePrinter(models.Model):
    '''

    '''