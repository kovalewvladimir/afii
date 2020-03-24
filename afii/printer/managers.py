from django.urls import reverse

from element.field import Field
from element.managers import ElementManager
from inventory.managers import TableManager
from inventory.table import Table, Cell, Button
from inventory.utils import get_status


class PrinterManager(ElementManager, TableManager):
    def get_table(self, space_id, model_fields=None, button=None, is_category=False):
        printers = self
        printers = printers.select_related()
        printers = printers.prefetch_related('base_printer__base_cartridges__cartridges__space')
        printers = printers.filter(is_active=True)
        printers = printers.filter(space__pk=space_id)

        table = Table()
        table.button = button
        table.header = [
            'Модель',
            'Тонер картридж',
            'Драм картридж',
            '№ Кабинета',
            'IP',
            'SN',
            'Тип печати',
            'Тип устройства',
            'Формат бумаги',
        ]

        for p in printers:
            table.append_row([
                Cell(p.base_printer.name, p.get_absolute_url()),
                Cell(items=p.get_items_cartridge('TONER')),
                Cell(items=p.get_items_cartridge('DRAM')),
                Cell(p.cabinet),
                Cell(p.ip, '//' + p.ip),
                Cell(p.sn),
                Cell(p.service),
                Cell(p.base_printer.get_type_printing_display),
                Cell(p.base_printer.get_type_display),
                Cell(p.base_printer.get_type_paper_display),
            ])

        return table

    def get_element(self, pk, model_fields):
        element = super().get_element(pk, model_fields)
        element.ip = self.element_db.ip

        table_cartridges = self.element_db.get_table_cartridges()
        element.table_toner_cartridge = table_cartridges['toner']
        element.table_dram_cartridge = table_cartridges['dram']
        element.table_zip = self.element_db.get_table_zip()
        return element


class CartridgeManager(ElementManager, TableManager):
    def get_table(self, space_id, model_fields=None, button=None, is_category=False):
        cartridges = self
        cartridges = cartridges.select_related()
        cartridges = cartridges.prefetch_related('base_cartridge__base_printers__printers__space')
        cartridges = cartridges.filter(is_active=True)
        cartridges = cartridges.filter(space__pk=space_id)

        table_t = Table(table_id='table-toner')
        table_d = Table(table_id='table-dram')
        table_s = Table(table_id='table-send-to-recycling')
        table_i = Table(table_id='table-in-recycling')

        table_t.button = Button(True, 'Добавить картридж', 'admin:printer_cartridge_add')
        table_d.button = Button(True, 'Добавить картридж', 'admin:printer_cartridge_add')
        table_s.button = Button(True, 'Отправить в рециклинг')
        table_i.button = Button(True, 'Вернуть из рециклинга')

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
                    Cell(items=c.get_item_printer())
                ])
                table_t.count += c.count
            if c.base_cartridge.type == 'DRAM':
                table_d.append_row([
                    Cell(c.base_cartridge.name, c.get_absolute_url()),
                    Cell(c.count, status=get_status(c.count, c.min_count)),
                    Cell(c.shelf),
                    Cell(items=c.get_item_printer())
                ])
                table_d.count += c.count
            if c.base_cartridge.recycling and c.base_cartridge.type != 'DRAM' and c.count_recycling > 0:
                table_s.append_row([
                    Cell(c.base_cartridge.name, c.get_absolute_url()),
                    Cell(c.count, status=get_status(c.count, c.min_count)),
                    Cell(c.count_recycling),
                    Cell(items=c.get_item_printer())
                ])
                table_s.count += c.count_recycling
            if c.base_cartridge.recycling and c.base_cartridge.type != 'DRAM' and c.count_in_recycling > 0:
                table_i.append_row([
                    Cell(c.base_cartridge.name, c.get_absolute_url()),
                    Cell(c.count_in_recycling),
                    Cell(items=c.get_item_printer())
                ])
                table_i.count += c.count_in_recycling

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

        element.table_printer = self.element_db.get_table_printer()

        return element


class ZipManager(ElementManager, TableManager):
    def get_table(self, space_id, model_fields=None, button=None, is_category=False):
        zip_db = self
        zip_db = zip_db.select_related()
        zip_db = zip_db.prefetch_related('base_zip__base_printers__printers__space')
        zip_db = zip_db.filter(is_active=True)
        zip_db = zip_db.filter(space__pk=space_id)

        table = Table()
        table.button = button
        table.header = [
            'Код',
            'Тип',
            'Кол-во',
            'Номер полки',
            'Модель принтера',
        ]

        for z in zip_db:
            table.append_row([
                Cell(z.base_zip, z.get_absolute_url()),
                Cell(z.base_zip.type),
                Cell(z.count, status=get_status(z.count, z.min_count)),
                Cell(z.shelf),
                Cell(items=z.get_item_printer()),
            ])

        return table

    def get_element(self, pk, model_fields):
        element = super().get_element(pk, model_fields)
        element.table_printer = self.element_db.get_table_printer()
        return element
