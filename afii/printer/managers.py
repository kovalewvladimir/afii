from django.db import models
from django.urls import reverse

from element.field import Field
from element.managers import ElementManager
from inventory.table import Table, Cell
from inventory.utils import get_status


class PrinterManager(ElementManager):
    def get_table(self, space_id):
        printers = self
        printers = printers.select_related()
        printers = printers.prefetch_related('base_printer__base_cartridges__cartridges__space')
        printers = printers.filter(is_active=True)
        printers = printers.filter(space__pk=space_id)

        table = Table()
        table.button_name = 'Добавить принтер'
        table.button_url = reverse('admin:printer_printer_add')
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
            table.append_row([
                Cell(p.base_printer.name, p.get_absolute_url()),
                Cell(items=p.get_items_cartridge(space_id, 'TONER')),
                Cell(items=p.get_items_cartridge(space_id, 'DRAM')),
                Cell(p.cabinet),
                Cell(p.ip, '//' + p.ip),
                Cell(p.base_printer.get_type_printing_display),
                Cell(p.base_printer.get_type_display),
                Cell(p.base_printer.get_type_paper_display),
            ])

        return table


class CartridgeManager(ElementManager):
    def get_table(self, space_id):
        cartridges = self
        cartridges = cartridges.select_related()
        cartridges = cartridges.prefetch_related('base_cartridge__base_printers__printers__space')
        cartridges = cartridges.filter(is_active=True)
        cartridges = cartridges.filter(space__pk=space_id)

        table_t = Table(table_id='table-toner')
        table_d = Table(table_id='table-dram')
        table_s = Table(table_id='table-send-to-recycling')
        table_i = Table(table_id='table-in-recycling')

        table_t.button_name = 'Добавить картридж'
        table_d.button_name = 'Добавить картридж'
        table_s.button_name = 'Отправить в рециклинг'
        table_i.button_name = 'Вернуть из рециклинга'

        table_t.button_url = reverse('admin:printer_cartridge_add')
        table_d.button_url = reverse('admin:printer_cartridge_add')

        table_t.header = [
            'Картридж',
            'Цвет',
            'Рециклинг',
            'В наличии',
            'Номер полки',
            'Модель принтера',
        ]
        table_d.header = [
            'Картридж',
            'В наличии',
            'Номер полки',
            'Модель принтера',
        ]
        table_s.header = [
            'Картридж',
            'В наличии',
            'В рециклинг',
            'Модель принтера',
        ]
        table_i.header = [
            'Картридж',
            'В рециклинге',
            'Модель принтера',
        ]

        for c in cartridges:
            if c.base_cartridge.type != 'DRAM':
                table_t.append_row([
                    Cell(c.base_cartridge.name, c.get_absolute_url()),
                    Cell(c.base_cartridge.get_color_display),
                    Cell(c.base_cartridge.recycling),
                    Cell(c.count, status=get_status(c.count, c.min_count)),
                    Cell(c.shelf),
                    Cell(items=c.get_printers(space_id))
                ])
                table_t.count += c.count
            if c.base_cartridge.type == 'DRAM':
                table_d.append_row([
                    Cell(c.base_cartridge.name, c.get_absolute_url()),
                    Cell(c.count, status=get_status(c.count, c.min_count)),
                    Cell(c.shelf),
                    Cell(items=c.get_printers(space_id))
                ])
                table_d.count += c.count
            if c.base_cartridge.recycling and c.base_cartridge.type != 'DRAM' and c.count_recycling > 0:
                table_s.append_row([
                    Cell(c.base_cartridge.name, c.get_absolute_url()),
                    Cell(c.count, status=get_status(c.count, c.min_count)),
                    Cell(c.count_recycling),
                    Cell(items=c.get_printers(space_id))
                ])
                table_s.count += c.count_recycling
            if c.base_cartridge.recycling and c.base_cartridge.type != 'DRAM' and c.count_in_recycling > 0:
                table_s.append_row([
                    Cell(c.base_cartridge.name, c.get_absolute_url()),
                    Cell(c.count_in_recycling),
                    Cell(items=c.get_printers(space_id))
                ])
                table_s.count += c.count_in_recycling

        tables = {
            'toner': table_t,
            'dram': table_d,
            'send_to_recycling': table_s,
            'in_recycling': table_i,
        }

        return tables

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
