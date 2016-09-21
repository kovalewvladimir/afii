from django.shortcuts import render, get_object_or_404, get_list_or_404
from inventory import models


def printers(request, space_id):
    space_id = int(space_id)

    args = {}
    args['space_id'] = space_id

    printers = models.Printer.objects
    printers = printers.select_related()
    printers = printers.prefetch_related('base_printer__base_cartridges__cartridges__space')
    printers = get_list_or_404(printers, space__pk=space_id)

    args['printers'] = printers

    return render(request, 'inventory/printers.html', args)


def cartridges(request, space_id):
    args = {}
    args['space_id'] = int(space_id)
    return render(request, 'inventory/.html', args)


def zips(request, space_id):
    args = {}
    args['space_id'] = int(space_id)
    return render(request, 'inventory/.html', args)


def papers(request, space_id):
    args = {}
    args['space_id'] = int(space_id)
    return render(request, 'inventory/.html', args)


def distributions(request, space_id):
    args = {}
    args['space_id'] = int(space_id)
    return render(request, 'inventory/.html', args)


def computers(request, space_id):
    args = {}
    args['space_id'] = int(space_id)
    return render(request, 'inventory/.html', args)


def printer(request, id):
    args = {}

    printers = models.Printer.objects
    printers = printers.select_related()
    #printers = printers.prefetch_related('base_printer__base_cartridges__cartridges__space')
    printers = get_object_or_404(printers, pk=id)

    args['printer'] = printers

    return render(request, 'inventory/printer.html', args)


def cartridge(request, id):
    args = {}
    return render(request, 'inventory/.html', args)


def zip(request, id):
    args = {}
    return render(request, 'inventory/.html', args)


def paper(request, id):
    args = {}
    return render(request, 'inventory/.html', args)


def distribution(request, id):
    args = {}
    return render(request, 'inventory/.html', args)


def computer(request, id):
    args = {}
    return render(request, 'inventory/.html', args)


# TODO: Удалить шаблон test, функцию main и url main
def main(request):
    args = {}
    args['title'] = 'test'

    printers = models.Printer.objects.select_related().prefetch_related(
        'base_printer__base_cartridges__cartridges').all()
    args['printers'] = printers
    return render(request, 'inventory/test.html', args)
