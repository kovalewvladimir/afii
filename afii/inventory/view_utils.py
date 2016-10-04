from django.urls import reverse
from django.contrib.staticfiles.templatetags.staticfiles import static


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


def default_filters(model, space_id):
    result = model.filter(delete=False)
    result = result.filter(space__pk=space_id)
    return result


def get_image_url(model):
    return model.image.url if model.image else static('inventory/img/default.png')


def get_table_printers(printers, space_id):
    if printers is None:
        return None

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
    for p in printers:
        table['value'].append([
            {'name': p.base_printer.name, 'link': reverse('inventory:printer', args=[p.pk])},
            {'for_items': [{'name': c.base_cartridge.name,
                            'link': reverse('inventory:cartridge', args=[c.pk])}
                           for bc in p.base_printer.base_cartridges.all()
                           if bc.type != 'DRAM'
                           for c in bc.cartridges.all()
                           if not c.delete and c.space.pk == space_id]},
            {'for_items': [{'name': c.base_cartridge.name,
                            'link': reverse('inventory:cartridge', args=[c.pk])}
                           for bc in p.base_printer.base_cartridges.all()
                           if bc.type == 'DRAM'
                           for c in bc.cartridges.all()
                           if not c.delete and c.space.pk == space_id]},
            {'name': p.cabinet},
            {'name': p.ip, 'link': '//' + p.ip},
            {'name': p.base_printer.get_type_printing_display},
            {'name': p.base_printer.get_type_display},
            {'name': p.base_printer.get_type_paper_display},
        ])
    return table


def get_table_cartridges(cartridges):
    if cartridges is None:
        return None

    table = {
        'header': [
            'Картридж',
            'Кол-во',
            'Номер полки',
            'Цвет тонера',
        ],
        'value': [],
        'status': 'success',
    }
    for t in cartridges:
        status = get_status(t.count, t.min_count)
        table['value'].append([
            {'name': t.base_cartridge.name, 'link': reverse('inventory:cartridge', args=[t.pk])},
            {'name': t.count, 'status': status},
            {'name': t.shelf},
            {'name': t.base_cartridge.get_color_display},
        ])
        table['status'] = get_status_table(table['status'], status)
    return table


def get_table_zips(zips, space_id=None, is_printers=False):
    if zips is None:
        return None

    table = {
        'header': [
            'Код',
            'Тип',
            'Кол-во',
            'Номер полки',
        ],
        'value': [],
        'status': 'success',
    }
    if is_printers:
        table['header'].append('Модель принтера')
    for z in zips:
        status = get_status(z.count, z.min_count)
        item = [{'name': z.base_zip.name, 'link': reverse('inventory:zip', args=[z.pk])},
                {'name': z.base_zip.type},
                {'name': z.count, 'status': status},
                {'name': z.shelf}]
        if is_printers:
            item.append({'for_items': [{'name': p.base_printer.name,
                                       'link': reverse('inventory:printer', args=[p.pk])}
                                       for bp in z.base_zip.base_printers.all()
                                       for p in bp.printers.all()
                                       if not p.delete and p.space.pk == space_id]})
        table['value'].append(item)
        table['status'] = get_status_table(table['status'], status)
    return table
