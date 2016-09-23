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
    p_db = models.Printer.objects
    p_db = p_db.select_related()
    p_db = get_object_or_404(p_db, pk=id)

    header = p_db.base_printer.name
    printer_ip = p_db.ip
    element = [
        {'name': '№ Кабинета',               'value': p_db.cabinet},
        {'name': 'Пользователь',              'value': p_db.user},
        {'name': 'IP',                        'value': p_db.ip, 'link': p_db.ip},
        {'name': 'User',                      'value': p_db.login},
        {'name': 'Password',                  'value': p_db.password},
        {'name': 'Тип печати',                'value': p_db.base_printer.get_type_printing_display},
        {'name': 'Цвет тонера',               'value': p_db.base_printer.get_color_display},
        {'name': 'Тип устройства',            'value': p_db.base_printer.get_type_display},
        {'name': 'Формат бумаги',             'value': p_db.base_printer.get_type_paper_display},
        {'name': 'Серийный номер',            'value': p_db.sn},
        {'name': 'Дата установки',            'value': p_db.date},
        {'name': 'Информация по расходникам', 'value': p_db.base_printer.info_consumables, 'link': p_db.base_printer.info_consumables},
        {'name': 'Примечание',                'value': p_db.description},
    ]

    toner_db = p_db.base_printer.base_cartridges.exclude(type='DRAM')
    dram_db = p_db.base_printer.base_cartridges.filter(type='DRAM')

    toner = list()

    for tc in toner_db:
        toner.append({
            'cartridge': tc.name,
            'count': tc.
            #todo:
        })

    args = {
        'element': element,
        'header': header,
        'printer_ip': printer_ip
    }
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
