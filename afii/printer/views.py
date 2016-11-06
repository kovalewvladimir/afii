from django.shortcuts import render, get_object_or_404

from element.views import ElementView
from printer import models


def printer_all_view(request, space_id):
    space = get_object_or_404(models.Space, pk=int(space_id))
    table = models.Printer.objects.get_table(int(space_id))

    args = {
        'space': space,
        'app_name': 'printer',
        'table': table,
    }

    return render(request, 'space/base_table.html', args)


def cartridge_all_view(request, space_id):
    space = get_object_or_404(models.Space, pk=int(space_id))

    args = {
        'space': space,
        'app_name': 'cartridge',
    }

    return render(request, 'space/base_table.html', args)


def zip_all_view(request, space_id):
    space = get_object_or_404(models.Space, pk=int(space_id))

    args = {
        'space': space,
        'app_name': 'zip',
    }

    return render(request, 'space/base_table.html', args)


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
