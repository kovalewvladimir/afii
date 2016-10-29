from django.db import models
from inventory.table import Table, Cell

from printer.models import *


class PrinterManager(models.Manager):
    def table(self, space_id):
        printer = self.filter(is_active=True)
        printer = printer.filter(space__pk=space_id)

        l = list(printer)

        table = Table()

        fields = printer.model._meta.fields

        for f in fields:
            table.header.append(f.verbose_name)

        for p in printer:
            table.rows.append(
                Cell('2'),
            )

        return table
