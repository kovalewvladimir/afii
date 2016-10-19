from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.db.models import Sum

from inventory import models
from inventory.view_utils import (default_filters,
                                  get_status,
                                  get_image_url,
                                  get_table_cartridges,
                                  get_table_printers,
                                  get_table_zips,)


def printers(request, space_id=1):
    space_id = int(space_id)
    name_space = get_object_or_404(models.Space, pk=space_id).name

    p_db = models.Printer.objects
    p_db = p_db.select_related()
    p_db = p_db.prefetch_related('base_printer__base_cartridges__cartridges__space')
    p_db = default_filters(p_db, space_id)

    table = get_table_printers(p_db, space_id)

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
    c_db = default_filters(c_db, space_id)

    table_stock = {
        'header': [
            'Картридж',
            'Тип',
            'Кол-во',
            'Номер полки',
            'Модель принтера',
        ],
        'value': [],
        'count': 0,
    }

    table_recycling = {
        'header': [
            'Картридж',
            'В наличии',
            'В рециклинг',
            'Модель принтера',
        ],
        'value': [],
        'count': 0,
    }

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
                           if not p.delete and p.space.pk == space_id]},
        ])
        table_stock['count'] += c.count
        if c.base_cartridge.recycling and c.base_cartridge.type != 'DRAM' and c.count_recycling > 0:
            table_recycling['value'].append([
                {'name': c.base_cartridge.name, 'link': reverse('inventory:cartridge', args=[c.pk])},
                {'name': c.count, 'status': get_status(c.count, c.min_count)},
                {'name': c.count_recycling},
                {'for_items': [{'name': p.base_printer.name,
                                'link': reverse('inventory:printer', args=[p.pk])}
                               for bp in c.base_cartridge.base_printers.all()
                               for p in bp.printers.all()
                               if p.delete and p.space.pk == space_id]},
            ])
            table_recycling['count'] += c.count_recycling

    args = {
        'space_id': space_id,
        'name_space': name_space,
        'btn_link_add': reverse('admin:inventory_cartridge_add'),
        'btn_name_add': 'Добавить картридж',
        'table_stock': table_stock,
        'table_recycling': table_recycling,
        'active_tab': 2,
    }
    return render(request, 'inventory/cartridges.html', args)


def zips(request, space_id):
    space_id = int(space_id)
    name_space = get_object_or_404(models.Space, pk=space_id).name

    z_db = models.Zip.objects
    z_db = z_db.select_related()
    z_db = z_db.prefetch_related('base_zip__base_printers__printers__space')
    z_db = default_filters(z_db, space_id)

    table = get_table_zips(z_db, space_id, True)

    args = {
        'space_id': space_id,
        'name_space': name_space,
        'table': table,
        'btn_link_add': reverse('admin:inventory_zip_add'),
        'btn_name_add': 'Добавить ЗИП',
        'active_tab': 3,
    }
    return render(request, 'inventory/space.html', args)


def papers(request, space_id):
    space_id = int(space_id)
    name_space = get_object_or_404(models.Space, pk=space_id).name

    p_db = models.Paper.objects
    p_db = default_filters(p_db, space_id)

    table = {
        'header': [
            'Номер',
            'Формат',
            'Размеры',
            'Кол-во рулонов',
        ],
        'value': [],
    }

    for p in p_db:
        table['value'].append([
            {'name': p.name, 'link': reverse('inventory:paper', args=[p.pk])},
            {'name': p.get_type_paper_display},
            {'name': p.size},
            {'name': p.count, 'status': get_status(p.count, p.min_count)},
        ])

    args = {
        'space_id': space_id,
        'name_space': name_space,
        'table': table,
        'btn_link_add': reverse('admin:inventory_paper_add'),
        'btn_name_add': 'Добавить бумагу',
        'active_tab': 4,
    }
    return render(request, 'inventory/space.html', args)


def distributions(request, space_id):
    space_id = int(space_id)
    name_space = get_object_or_404(models.Space, pk=space_id).name

    d_db = models.Distribution.objects
    d_db = default_filters(d_db, space_id)

    table = {
        'header': [
            '№',
            'Наименование',
            'Кол-во',
        ],
        'value': [],
    }

    for d in d_db:
        table['value'].append([
            {'name': d.pk},
            {'name': d.name, 'link': reverse('inventory:distribution', args=[d.pk])},
            {'name': d.count},
        ])

    args = {
        'space_id': space_id,
        'name_space': name_space,
        'table': table,
        'btn_link_add': reverse('admin:inventory_distribution_add'),
        'btn_name_add': 'Добавить дистрибутив',
        'active_tab': 5,
    }
    return render(request, 'inventory/space.html', args)


def computers(request, space_id):
    space_id = int(space_id)
    name_space = get_object_or_404(models.Space, pk=space_id).name

    c_db = models.Computer.objects
    c_db = default_filters(c_db, space_id)

    table = {
        'header': [
            '№',
            'Процессор',
            'Материнская плата',
            'Оперативная память',
            'Видеокарта',
            'Наклейка лицензии',
            'Блок питания',
        ],
        'value': [],
    }

    for c in c_db:
        table['value'].append([
            {'name': c.pk, 'link': reverse('inventory:computer', args=[c.pk])},
            {'name': c.cpu},
            {'name': c.motherboard},
            {'name': c.ram},
            {'name': c.gpu},
            {'name': c.license_sticker},
            {'name': c.power_supply},
        ])

    args = {
        'space_id': space_id,
        'name_space': name_space,
        'table': table,
        'btn_link_add': reverse('admin:inventory_computer_add'),
        'btn_name_add': 'Добавить компьютер',
        'active_tab': 6,
    }
    return render(request, 'inventory/space.html', args)


def storage(request, space_id, id_storage):
    space_id = int(space_id)
    name_space = get_object_or_404(models.Space, pk=space_id).name

    is_db = models.ItemStorage.objects
    is_db = is_db.select_related()
    is_db = is_db.filter(delete=False)
    is_db = is_db.filter(category__storage__space__id=space_id)

    c_db = models.Category.objects
    c_db = c_db.select_related()
    c_db = c_db.prefetch_related('categories')
    c_db = c_db.filter(is_base=True)
    c_db = c_db.filter(storage__pk=id_storage)

    category = list()
    count_all = 0
    for c in c_db:
        item = {
            'name': c.name,
            'for_items': list(),
        }
        sum_count = 0
        for i in c.categories.all():
            #count = i.items.all().aggregate(Sum('count'))['count__sum']
            count = 0 #i.items.count()
            item['for_items'].append({
                'name': i.name,
                'count': count,
            })
            sum_count += count
        item['count'] = sum_count
        count_all += sum_count
        category.append(item)

    table = {
        'header': [
            '№',
            'Наименование',
            'Кол-во',
            'Номер полки',
        ],
        'value': [],
    }

    for i in is_db:
        table['value'].append([
            {'name': i.pk},
            {'name': i.name},
            {'name': i.count},
            {'name': i.shelf},
        ])

    args = {
        'space_id': space_id,
        'name_space': name_space,
        'table': table,
        'category': category,
        'count_all': count_all,
    }
    return render(request, 'inventory/storage.html', args)


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

    table_toner = get_table_cartridges(toner_db)
    table_dram = get_table_cartridges(dram_db)
    table_zip = get_table_zips(zip_db)

    args = {
        'elements': elements,
        'name_element': name_element,
        'type_element': 'Принтер',
        'link_image_element': get_image_url(p_db),
        'link_edit_element': reverse('admin:inventory_printer_change', args=(id_printer,)),
        'printer_ip': printer_ip,
        'table_toner': table_toner,
        'table_dram': table_dram,
        'table_zip': table_zip,
        'space_id': p_db.space.pk,
    }
    return render(request, 'inventory/printer.html', args)


def cartridge(request, id_cartridge):
    c_db = models.Cartridge.objects
    c_db = c_db.select_related()
    c_db = get_object_or_404(c_db, pk=id_cartridge)

    space_id = c_db.space.pk

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

    p_db = c_db.get_printers()
    table_printers = get_table_printers(p_db, space_id)

    args = {
        'elements': elements,
        'name_element': name_element,
        'type_element': 'Картридж',
        'table_printers': table_printers,
        'link_image_element': get_image_url(c_db),
        'link_edit_element': reverse('admin:inventory_cartridge_change', args=(id_cartridge,)),
        'space_id': space_id,
    }
    return render(request, 'inventory/cartridge_or_zip.html', args)


def zip(request, id_zip):
    z_db = models.Zip.objects
    z_db = z_db.select_related()
    z_db = get_object_or_404(z_db, pk=id_zip)

    space_id = z_db.space.pk

    name_element = z_db.base_zip.name
    elements = [
        {'name': 'Тип', 'value': z_db.base_zip.type},
        {'name': '№ полки', 'value': z_db.shelf},
        {'name': 'Кол-во', 'value': z_db.count, 'status': get_status(z_db.count, z_db.min_count)},
        {'name': 'Минимальное кол-во', 'value': z_db.min_count},
        {'name': 'Примечание', 'value': z_db.description},
    ]

    p_db = z_db.get_printers()
    table_printers = get_table_printers(p_db, space_id)

    args = {
        'elements': elements,
        'name_element': name_element,
        'type_element': 'ЗИП',
        'table_printers': table_printers,
        'link_image_element': get_image_url(z_db),
        'link_edit_element': reverse('admin:inventory_zip_change', args=(id_zip,)),
        'space_id': space_id,
    }
    return render(request, 'inventory/cartridge_or_zip.html', args)


def paper(request, id_paper):
    p_db = models.Paper.objects
    p_db = p_db.select_related()
    p_db = get_object_or_404(p_db, pk=id_paper)

    space_id = p_db.space.pk

    name_element = p_db.name
    elements = [
        {'name': 'Формат', 'value': p_db.get_type_paper_display},
        {'name': 'Размеры', 'value': p_db.size},
        {'name': 'Кол-во', 'value': p_db.count, 'status': get_status(p_db.count, p_db.min_count)},
        {'name': 'Минимальное кол-во', 'value': p_db.min_count},
        {'name': 'Примечание', 'value': p_db.description},
    ]

    args = {
        'elements': elements,
        'name_element': name_element,
        'type_element': 'Бумага',
        'link_image_element': get_image_url(p_db),
        'link_edit_element': reverse('admin:inventory_paper_change', args=(id_paper,)),
        'space_id': space_id,
    }
    return render(request, 'inventory/elements.html', args)


def distribution(request, id_distribution):
    d_db = models.Distribution.objects
    d_db = d_db.select_related()
    d_db = get_object_or_404(d_db, pk=id_distribution)

    space_id = d_db.space.pk

    name_element = d_db.name
    elements = [
        {'name': 'Наименование', 'value': d_db.name},
        {'name': 'Кол-во', 'value': d_db.count},
    ]

    args = {
        'elements': elements,
        'name_element': name_element,
        'type_element': 'Дистрибутивы',
        'link_image_element': get_image_url(d_db),
        'link_edit_element': reverse('admin:inventory_distribution_change', args=(id_distribution,)),
        'space_id': space_id,
    }
    return render(request, 'inventory/elements.html', args)


def computer(request, id_computer):
    c_db = models.Computer.objects
    c_db = c_db.select_related()
    c_db = get_object_or_404(c_db, pk=id_computer)

    space_id = c_db.space.pk

    name_element = c_db.pk
    elements = [
        {'name': '№', 'value': c_db.pk},
        {'name': 'Процессор', 'value': c_db.cpu},
        {'name': 'Материнская плата', 'value': c_db.motherboard},
        {'name': 'Оперативная память', 'value': c_db.ram},
        {'name': 'Видеокарта', 'value': c_db.gpu},
        {'name': 'Сетевой адаптер', 'value': c_db.get_lan_display if c_db.lan else ''},
        {'name': 'Блок питания', 'value': c_db.power_supply},
        {'name': 'Наклейка лицензии', 'value': c_db.license_sticker},
        {'name': 'Жесткий диск', 'value': c_db.hdd},
        {'name': 'Операционная система', 'value': c_db.os},
        {'name': 'Примечание', 'value': c_db.description},
    ]

    args = {
        'elements': elements,
        'name_element': name_element,
        'type_element': 'Системные блоки',
        'link_image_element': get_image_url(c_db),
        'link_edit_element': reverse('admin:inventory_computer_change', args=(id_computer,)),
        'space_id': space_id,
    }
    return render(request, 'inventory/elements.html', args)
