from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse

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
    def get_status(current, minimum):
        if current > minimum:
            return 'success'
        elif current < minimum:
            return 'danger'
        elif current == minimum:
            return 'warning'

    def get_status_table(current, new):
        if new == 'warning':
            if current != 'danger':
                return 'warning'
        if new == 'danger':
                return 'danger'
        else:
            return current

    p_db = models.Printer.objects
    p_db = p_db.select_related()
    p_db = get_object_or_404(p_db, pk=id)

    header = p_db.base_printer.name
    printer_ip = p_db.ip
    element = [
        {'name': '№ Кабинета', 'value': p_db.cabinet},
        {'name': 'Пользователь', 'value': p_db.user},
        {'name': 'IP', 'value': p_db.ip, 'link': p_db.ip},
        {'name': 'User', 'value': p_db.login},
        {'name': 'Password', 'value': p_db.password},
        {'name': 'Тип печати', 'value': p_db.base_printer.get_type_printing_display},
        {'name': 'Цвет тонера', 'value': p_db.base_printer.get_color_display},
        {'name': 'Тип устройства', 'value': p_db.base_printer.get_type_display},
        {'name': 'Формат бумаги', 'value': p_db.base_printer.get_type_paper_display},
        {'name': 'Серийный номер', 'value': p_db.sn},
        {'name': 'Дата установки', 'value': '' if p_db.date is None else p_db.date},
        {'name': 'Информация по расходникам', 'value': p_db.base_printer.info_consumables,
         'link': p_db.base_printer.info_consumables},
        {'name': 'Примечание', 'value': p_db.description},
    ]

    toner_db = p_db.get_cartridges()
    dram_db = p_db.get_dram_cartridges()
    zip_db = p_db.get_zips()

    toner, toner_table_status = None, None
    if toner_db is not None:
        toner = list()
        toner_table_status = 'success'
        for t in toner_db:
            status = get_status(t.count, t.min_count)
            value = {
                'name': t.base_cartridge.name,
                'link': reverse('inventory:cartridge', args=[t.pk]),
                'count': t.count,
                'shelf': t.shelf,
                'color': t.base_cartridge.get_color_display,
                'status': status,
            }
            toner_table_status = get_status_table(toner_table_status, status)
            toner.append(value)

    if dram_db is not None:
        dram = list()
        dram_table_status = 'success'
        for d in dram_db:
            status = get_status(d.count, d.min_count)
            value = {
                'name': d.base_cartridge.name,
                'link': reverse('inventory:cartridge', args=[d.pk]),
                'count': d.count, 'shelf': d.shelf,
                'status': status,
            }
            dram_table_status = get_status_table(dram_table_status, status)
            dram.append(value)
    else:
        dram, dram_table_status = None, None

    if zip_db is not None:
        zip = list()
        zip_table_status = 'success'
        for z in zip_db:
            status = get_status(z.count, z.min_count)
            value = {
                'name': z.base_zip.name,
                'link': reverse('inventory:zip', args=[z.pk]),
                'type': z.base_zip.type,
                'count': z.count,
                'shelf': z.shelf,
                'status': status,
            }
            zip_table_status = get_status_table(zip_table_status, status)
            zip.append(value)
    else:
        zip, zip_table_status = None, None

    args = {
        'element': element,
        'header': header,
        'printer_ip': printer_ip,
        'toner': toner,
        'toner_table_status': toner_table_status,
        'dram': dram,
        'dram_table_status': dram_table_status,
        'zip': zip,
        'zip_table_status': zip_table_status,
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
