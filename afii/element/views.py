from django.shortcuts import render

from element import models


def paper_view(request, paper_id):
    model_fields = [
        'name',
        'space',
        'type_paper',
        'size',
        'count',
        'min_count',
        'description',
        'is_active',
    ]

    element = models.Paper.objects.get_element(paper_id, model_fields)

    args = {
        'element': element,
    }

    return render(request, 'element/base.html', args)


def distribution_view(request, paper_id):
    model_fields = [
        'name',
        'space',
        'count',
        'is_active',
    ]

    element = models.Distribution.objects.get_element(paper_id, model_fields)

    args = {
        'element': element,
    }

    return render(request, 'element/base.html', args)


def computer_view(request, paper_id):
    model_fields = [
        'cpu',
        'space',
        'motherboard',
        'ram',
        'gpu',
        'lan',
        'power_supply',
        'license_sticker',
        'hdd',
        'os',
        'description',
        'is_active',
    ]

    element = models.Computer.objects.get_element(paper_id, model_fields)

    args = {
        'element': element,
    }

    return render(request, 'element/base.html', args)


