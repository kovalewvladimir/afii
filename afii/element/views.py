from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from element import models
from inventory.table import Button
from inventory.views import TableView


@method_decorator(login_required, name='dispatch')
class ElementView(ListView):
    model = None
    model_fields = None
    template_name = 'element/base.html'
    context_object_name = 'element'

    def get_queryset(self):
        return self.model.objects.get_element(self.args[0], self.model_fields)


class PaperAllView(TableView):
    model = models.Paper
    model_fields = [
        {'model': 'self', 'field': 'name', 'url': True},
        {'model': 'self', 'field': 'type_paper'},
        {'model': 'self', 'field': 'size'},
        {'model': 'self', 'field': 'count', 'status': True},
    ]
    app_name = 'paper'
    button = Button(True, 'Добавить бумагу', 'admin:element_paper_add')


class DistributionAllView(TableView):
    model = models.Distribution
    model_fields = [
        {'model': 'self', 'field': 'id'},
        {'model': 'self', 'field': 'name', 'url': True},
        {'model': 'self', 'field': 'count'},
    ]
    app_name = 'distribution'
    button = Button(True, 'Добавить дистрибутив', 'admin:element_distribution_add')


class ComputerAllView(TableView):
    model = models.Computer
    model_fields = [
        {'model': 'self', 'field': 'id', 'url': True},
        {'model': 'self', 'field': 'cpu'},
        {'model': 'self', 'field': 'motherboard'},
        {'model': 'self', 'field': 'ram'},
        {'model': 'self', 'field': 'gpu'},
        {'model': 'self', 'field': 'license_sticker'},
        {'model': 'self', 'field': 'power_supply'},
    ]
    app_name = 'computer'
    button = Button(True, 'Добавить системый блок', 'admin:element_computer_add')


class PaperView(ElementView):
    model = models.Paper
    model_fields = [
        {'model': 'self', 'field': 'name'},
        {'model': 'self', 'field': 'space'},
        {'model': 'self', 'field': 'type_paper'},
        {'model': 'self', 'field': 'size'},
        {'model': 'self', 'field': 'count', 'status': True},
        {'model': 'self', 'field': 'min_count'},
        {'model': 'self', 'field': 'is_active'},
        {'model': 'self', 'field': 'description'},
    ]


class DistributionView(ElementView):
    model = models.Distribution
    model_fields = [
        {'model': 'self', 'field': 'name'},
        {'model': 'self', 'field': 'space'},
        {'model': 'self', 'field': 'count'},
        {'model': 'self', 'field': 'is_active'},
        {'model': 'self', 'field': 'description'},
    ]


class ComputerView(ElementView):
    model = models.Computer
    model_fields = [
        {'model': 'self', 'field': 'cpu'},
        {'model': 'self', 'field': 'space'},
        {'model': 'self', 'field': 'motherboard'},
        {'model': 'self', 'field': 'ram'},
        {'model': 'self', 'field': 'gpu'},
        {'model': 'self', 'field': 'lan'},
        {'model': 'self', 'field': 'power_supply'},
        {'model': 'self', 'field': 'license_sticker'},
        {'model': 'self', 'field': 'hdd'},
        {'model': 'self', 'field': 'os'},
        {'model': 'self', 'field': 'is_active'},
        {'model': 'self', 'field': 'description'},
    ]
