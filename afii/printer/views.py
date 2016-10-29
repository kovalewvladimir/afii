from django.shortcuts import render, get_object_or_404
from printer import models
from inventory.table import Table, Rows, Cell, Items


def printer_all_view(request, space_id):
    space = get_object_or_404(models.Space, pk=int(space_id))
    printers = space.printers.all()

    table = models.Printer.objects.table(space.pk)


    printers_c = printers.count()


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
