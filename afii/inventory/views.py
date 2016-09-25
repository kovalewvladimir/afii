from django.contrib.staticfiles.templatetags.staticfiles import static
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse

from inventory import models


# TODO: Убрать функции get_status, get_status_table в отдельный пакет
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


def printers(request, space_id=1):
    space_id = int(space_id)
    name_space = get_object_or_404(models.Space, pk=space_id).name

    p_db = models.Printer.objects
    p_db = p_db.select_related()
    p_db = p_db.prefetch_related('base_printer__base_cartridges__cartridges__space')
    p_db = p_db.filter(delete=False)
    p_db = get_list_or_404(p_db, space__pk=space_id)

    table = {
        'header': [
            'Модель',
            'Тонер картридж',
            'Драм картридж',
            '№ Кабинета',
            'IP',
            'Тип печати',
            'Тип устройства',
            'Формат бумаги',
        ],
        'value': [],
    }

    for p in p_db:
        table['value'].append([
            {'name': p.base_printer.name, 'link': reverse('inventory:printer', args=[p.pk])},
            {'for_items': [{'name': c.base_cartridge.name,
                            'link': reverse('inventory:cartridge', args=[c.pk])}
                           for bc in p.base_printer.base_cartridges.all()
                           for c in bc.cartridges.all()
                           if c.base_cartridge.type != 'DRAM'
                           if c.space.pk == space_id]},
            {'for_items': [{'name': c.base_cartridge.name,
                            'link': reverse('inventory:cartridge', args=[c.pk])}
                           for bc in p.base_printer.base_cartridges.all()
                           for c in bc.cartridges.all()
                           if c.base_cartridge.type == 'DRAM'
                           if c.space.pk == space_id]},
            {'name': p.cabinet},
            {'name': p.ip, 'link': '//' + p.ip},
            {'name': p.base_printer.get_type_printing_display},
            {'name': p.base_printer.get_type_display},
            {'name': p.base_printer.get_type_paper_display},
        ])

    args = {
        'space_id': space_id,
        'name_space': name_space,
        'btn_link_add': reverse('admin:inventory_printer_add'),
        'btn_name_add': 'Добавить принтер',
        'table': table,
        'active_tab': 1,
    }
    return render(request, 'inventory/space.html', args)


def cartridges(request, space_id):
    space_id = int(space_id)
    name_space = get_object_or_404(models.Space, pk=space_id).name

    c_db = models.Cartridge.objects
    c_db = c_db.select_related()
    c_db = c_db.prefetch_related('base_cartridge__base_printers__printers__space')
    c_db = c_db.filter(delete=False)
    c_db = c_db.filter(space__pk=space_id)

    table_stock = {
        'header': [
            'Картридж',
            'Тип',
            'Кол-во',
            'Номер полки',
            'Модель принтера',
        ],
        'value': [],
    }

    table_recycling = {
        'header': [
            'Картридж',
            'В наличии',
            'В рециклинг',
            'Модель принтера',
        ],
        'value': [],
    }

    count_stock, count_recycling = 0, 0
    for c in c_db:
        table_stock['value'].append([
            {'name': c.base_cartridge.name, 'link': reverse('inventory:cartridge', args=[c.pk])},
            {'name': c.base_cartridge.get_type_display},
            {'name': c.count, 'status': get_status(c.count, c.min_count)},
            {'name': c.shelf},
            {'for_items': [{'name': p.base_printer.name,
                            'link': reverse('inventory:printer', args=[p.pk])}
                           for bp in c.base_cartridge.base_printers.all()
                           for p in bp.printers.all()
                           if p.space.pk == space_id]},
        ])
        count_stock += c.count
        if c.base_cartridge.recycling and c.base_cartridge.type != 'DRAM' and c.count_recycling > 0:
            table_recycling['value'].append([
                {'name': c.base_cartridge.name, 'link': reverse('inventory:cartridge', args=[c.pk])},
                {'name': c.count, 'status': get_status(c.count, c.min_count)},
                {'name': c.count_recycling},
                {'for_items': [{'name': p.base_printer.name,
                                'link': reverse('inventory:printer', args=[p.pk])}
                               for bp in c.base_cartridge.base_printers.all()
                               for p in bp.printers.all()
                               if p.space.pk == space_id]},
            ])
            count_recycling += c.count_recycling

    args = {
        'space_id': space_id,
        'name_space': name_space,
        'btn_link_add': reverse('admin:inventory_cartridge_add'),
        'btn_name_add': 'Добавить картридж',
        'table_stock': table_stock,
        'table_recycling': table_recycling,
        'count_stock': count_stock,
        'count_recycling': count_recycling,
        'active_tab': 2,
    }
    return render(request, 'inventory/cartridges.html', args)


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


def printer(request, id_printer):
    p_db = models.Printer.objects
    p_db = p_db.select_related()
    p_db = get_object_or_404(p_db, pk=id_printer)

    name_element = p_db.base_printer.name
    printer_ip = p_db.ip
    elements = [
        {'name': '№ Кабинета', 'value': p_db.cabinet},
        {'name': 'Пользователь', 'value': p_db.user},
        {'name': 'IP', 'value': printer_ip, 'link': printer_ip},
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
        'elements': elements,
        'name_element': name_element,
        'type_element': 'Принтер',
        'link_image_element': p_db.image.url if p_db.image else static('inventory/img/default.png'),
        'link_edit_element': reverse('admin:inventory_printer_change', args=(id_printer,)),
        'printer_ip': printer_ip,
        'toner': toner,
        'toner_table_status': toner_table_status,
        'dram': dram,
        'dram_table_status': dram_table_status,
        'zip': zip,
        'zip_table_status': zip_table_status,
        'space_id': p_db.space.pk,
    }
    return render(request, 'inventory/printer.html', args)


def cartridge(request, id_cartridge):
    c_db = models.Cartridge.objects
    c_db = c_db.select_related()
    c_db = get_object_or_404(c_db, pk=id_cartridge)

    name_element = c_db.base_cartridge.name
    elements = [
        {'name': 'Тип', 'value': c_db.base_cartridge.get_type_display},
        {'name': '№ полки', 'value': c_db.shelf},
        {'name': 'Кол-во', 'value': c_db.count, 'status': get_status(c_db.count, c_db.min_count)},
        {'name': 'Минимальное кол-во', 'value': c_db.min_count},
        {'name': 'Примечание', 'value': c_db.description},
    ]

    if c_db.base_cartridge.type != 'DRAM':
        recycling = c_db.base_cartridge.recycling
        elements.insert(2, {'name': 'Цвет тонера', 'value': c_db.base_cartridge.get_color_display})
        elements.insert(3, {'name': 'Рециклинг', 'value': 'Да' if recycling else 'Нет'})
        if recycling:
            elements.insert(4, {'name': 'Кол-во в рециклинг', 'value': c_db.count_recycling})

    args = {
        'elements': elements,
        'name_element': name_element,
        'type_element': 'Картридж',
        'link_image_element': c_db.image.url if c_db.image else static('inventory/img/default.png'),
        'link_edit_element': reverse('admin:inventory_cartridge_change', args=(id_cartridge,)),
        'space_id': c_db.space.pk,
    }
    return render(request, 'inventory/elements.html', args)


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
