from django.shortcuts import render
from django.utils.decorators import classonlymethod
from django.views.generic import ListView

from element import models


class ElementView(ListView):
    model = None
    model_fields = None
    template_name = 'element/base.html'
    context_object_name = 'element'

    def get_queryset(self):
        return self.model.objects.get_element(self.args[0], self.model_fields)


class PaperView(ElementView):
    model = models.Paper
    model_fields = {
        'self': [
            'name',
            'space',
            'type_paper',
            'size',
            'count',
            'min_count',
            'description',
            'is_active',
        ],
    }


class DistributionView(ElementView):
    model = models.Distribution
    model_fields = [
        'name',
        'space',
        'count',
        'is_active',
    ]


class ComputerView(ElementView):
    model = models.Computer
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


def all_view(request, paper_id):
    pass
