from django.shortcuts import render, get_object_or_404

from element.views import ElementView
from printer import models
from space.views import TableView


class PrinterAllView(TableView):
    model = models.Printer
    app_name = 'printer'


class CartridgeAllView(TableView):
    model = models.Cartridge
    app_name = 'cartridge'
    template_name = 'printer/cartridge_all.html'
    context_object_name = 'tables'


class ZipAllView(TableView):
    model = models.Zip
    app_name = 'zip'


class PrinterView(ElementView):
    model = models.Printer
    model_fields = [
        {'model': 'self', 'field': 'base_printer'},
        {'model': 'self', 'field': 'space'},
        {'model': 'self', 'field': 'cabinet'},
        {'model': 'base_printer', 'field': 'type_printing'},
        {'model': 'base_printer', 'field': 'type'},
        {'model': 'base_printer', 'field': 'color'},
        {'model': 'base_printer', 'field': 'type_paper'},
        {'model': 'self', 'field': 'user'},
        {'model': 'self', 'field': 'login'},
        {'model': 'self', 'field': 'password'},
        {'model': 'self', 'field': 'ip'},
        {'model': 'self', 'field': 'sn'},
        {'model': 'self', 'field': 'date'},
        {'model': 'self', 'field': 'is_active'},
        {'model': 'base_printer', 'field': 'info_consumables'},
        {'model': 'self', 'field': 'description'},
    ]

    def get_context_data(self, **kwargs):
        context = super(PrinterView, self).get_context_data(**kwargs)
        # TODO: cartridge and zip get_table()
        context['123'] = '123'
        return context


class CartridgeView(ElementView):
    model = models.Cartridge
    model_fields = [
        {'model': 'self', 'field': 'base_cartridge'},
        {'model': 'self', 'field': 'space'},
        {'model': 'self', 'field': 'shelf'},
        {'model': 'base_cartridge', 'field': 'type'},
        {'model': 'self', 'field': 'count'},
        {'model': 'self', 'field': 'min_count'},
        {'model': 'self', 'field': 'is_active'},
        {'model': 'self', 'field': 'description'},
    ]


class ZipView(ElementView):
    model = models.Zip
    model_fields = [
        'base_zip',
        'space',
        'shelf',
        'count',
        'min_count',
        'description',
        'is_active',
    ]
