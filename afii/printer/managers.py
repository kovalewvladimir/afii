from django.db import models
from django.urls import reverse

from element.field import Field
from element.managers import ElementManager
from inventory.table import Table, Cell


class PrinterManager(ElementManager):
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
            table.append_row(
                Cell(p.base_printer.name, p.get_absolute_url()),
                Cell(items=p.get_items_cartridge(space_id, 'TONER')),
                Cell(items=p.get_items_cartridge(space_id, 'DRAM')),
                Cell(p.cabinet),
                Cell(p.ip, '//' + p.ip),
                Cell(p.base_printer.get_type_printing_display),
                Cell(p.base_printer.get_type_display),
                Cell(p.base_printer.get_type_paper_display)
            )

        return table


class CartridgeManager(ElementManager):
    def get_table(self, space_id):
        pass

    def get_element(self, pk, model_fields):
        element = super().get_element(pk, model_fields)
        is_toner = self.element_db.base_cartridge.type != 'DRAM'
        is_recycling = self.element_db.base_cartridge.recycling

        if is_toner:
            field = Field()
            field.name = self.element_db.base_cartridge.get_field('color')
            field.value = self.element_db.base_cartridge.get_color_display()
            element.fields.insert(4, field)
            field = Field()
            field.name = self.element_db.base_cartridge.get_field('recycling')
            field.value = self.element_db.base_cartridge.recycling
            element.fields.insert(5, field)

        if is_recycling:
            field = Field()
            field.name = self.element_db.get_field('count_recycling')
            field.value = self.element_db.count_recycling
            element.fields.insert(8, field)

        return element
