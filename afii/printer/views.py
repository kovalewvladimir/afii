from element.views import ElementView
from inventory.table import Button
from printer import models
from inventory.views import TableView


class PrinterAllView(TableView):
    model = models.Printer
    app_name = 'printer'
    button = Button(True, 'Добавить принтер', 'admin:printer_printer_add')


class CartridgeAllView(TableView):
    model = models.Cartridge
    app_name = 'cartridge'
    template_name = 'printer/cartridge_all.html'
    context_object_name = 'tables'


class ZipAllView(TableView):
    model = models.Zip
    app_name = 'zip'
    button = Button(True, 'Добавить ЗИП', 'admin:printer_zip_add')


class PrinterView(ElementView):
    model = models.Printer
    model_fields = [
        {'model': 'self', 'field': 'base_printer'},
        {'model': 'self', 'field': 'space'},
        {'model': 'self', 'field': 'cabinet'},
        {'model': 'self', 'field': 'user'},
        {'model': 'base_printer', 'field': 'type_printing'},
        {'model': 'base_printer', 'field': 'type'},
        {'model': 'base_printer', 'field': 'color'},
        {'model': 'base_printer', 'field': 'type_paper'},
        {'model': 'self', 'field': 'ip', 'url': True},
        {'model': 'self', 'field': 'login'},
        {'model': 'self', 'field': 'password'},
        {'model': 'self', 'field': 'sn'},
        {'model': 'self', 'field': 'date'},
        {'model': 'self', 'field': 'is_active'},
        {'model': 'base_printer', 'field': 'info_consumables', 'url': True},
        {'model': 'self', 'field': 'description'},
    ]
    template_name = 'printer/printer.html'


class CartridgeView(ElementView):
    model = models.Cartridge
    model_fields = [
        {'model': 'self', 'field': 'base_cartridge'},
        {'model': 'self', 'field': 'space'},
        {'model': 'self', 'field': 'shelf'},
        {'model': 'base_cartridge', 'field': 'type'},
        {'model': 'self', 'field': 'count', 'status': True},
        {'model': 'self', 'field': 'min_count'},
        {'model': 'self', 'field': 'is_active'},
        {'model': 'self', 'field': 'description'},
    ]
    template_name = 'printer/cartridge_or_zip.html'


class ZipView(ElementView):
    model = models.Zip
    model_fields = [
        {'model': 'self', 'field': 'base_zip'},
        {'model': 'base_zip', 'field': 'type'},
        {'model': 'self', 'field': 'space'},
        {'model': 'self', 'field': 'shelf'},
        {'model': 'self', 'field': 'count', 'status': True},
        {'model': 'self', 'field': 'min_count'},
        {'model': 'self', 'field': 'is_active'},
        {'model': 'self', 'field': 'description'},
    ]
    template_name = 'printer/cartridge_or_zip.html'
