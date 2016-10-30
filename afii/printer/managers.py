from django.db import models
from django.urls import reverse

from inventory.table import Table, Cell


class PrinterManager(models.Manager):
    def get_table(self, space_id):
        printers = self
        printers = printers.select_related()
        printers = printers.prefetch_related('base_printer__base_cartridges__cartridges__space')
        printers = printers.filter(is_active=True)
        printers = printers.filter(space__pk=space_id)

        table = Table()
        table.header = [
            'Модель',
            'Тонер картридж',
            'Драм картридж',
            '№ Кабинета',
            'IP',
            'Тип печати',
            'Тип устройства',
            'Формат бумаги',
        ]

        for p in printers:
            table.append(
                Cell(p.base_printer.name, reverse('printer:printer', args=[p.pk])),
                Cell(items=p.get_items_toner_cartridge(space_id)),
                Cell(items=p.get_items_dram_cartridge(space_id)),
                Cell(p.cabinet),
                Cell(p.ip, '//' + p.ip),
                Cell(p.base_printer.get_type_printing_display),
                Cell(p.base_printer.get_type_display),
                Cell(p.base_printer.get_type_paper_display)
            )

        return table
