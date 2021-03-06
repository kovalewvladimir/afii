from django.http import Http404
from django.shortcuts import redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import ListView

from element import models
from inventory.table import Button
from inventory.views import TableView


@method_decorator(login_required, name='dispatch')
class ElementView(ListView):
    """
    Базовый класс представления, отвечающий за вывод подробной
    информации об элементе.  Модель, над которой работает данный
    класс, должна реализовать менеджер ElementManager.
    Атрибуты:
        model – модель для вывода;
        model_fields – поля для вывода;
        template_name – шаблон для отображения;
        context_object_name – имя элемента, передаваемое в шаблон;
    """
    model = None
    model_fields = None
    template_name = 'element/base.html'
    context_object_name = 'element'

    def get_queryset(self):
        return self.model.objects.get_element(self.args[0], self.model_fields)


@method_decorator(login_required, name='dispatch')
class ElementMinusView(View):
    """
    Базовый класс представления, отвечающий за уменьшение
    количества элементов на складе.
    Атрибуты:
        model –модель для редактирования;
    """
    model = None

    def post(self, request, *args, **kwargs):
        if self.model is None:
            raise Http404()
        object_element = get_object_or_404(self.model, pk=int(args[0]))
        object_element.count -= 1
        if object_element.count >= 0:
            object_element.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))

    def get(self, request, *args, **kwargs):
        raise Http404()


class PaperAllView(TableView):
    """
    Класс представления, отвечающий за вывод таблицы с бумагой
    """
    model = models.Paper
    model_fields = [
        {'model': 'self', 'field': 'type_paper', 'url': True},
        {'model': 'self', 'field': 'name'},
        {'model': 'self', 'field': 'size'},
        {'model': 'self', 'field': 'count', 'status': True},
    ]
    app_name = 'paper'
    button = Button(True, 'Добавить бумагу', 'admin:element_paper_add')


class DistributionAllView(TableView):
    """
    Класс представления, отвечающий за вывод таблицы с дистрибутивами
    """
    model = models.Distribution
    model_fields = [
        {'model': 'self', 'field': 'id'},
        {'model': 'self', 'field': 'name', 'url': True},
        {'model': 'self', 'field': 'count'},
    ]
    app_name = 'distribution'
    button = Button(True, 'Добавить дистрибутив', 'admin:element_distribution_add')


class ComputerAllView(TableView):
    """
    Класс представления, отвечающий за вывод таблицы с системными блоками
    """
    model = models.Computer
    model_fields = [
        {'model': 'self', 'field': 'id', 'url': True},
        {'model': 'self', 'field': 'cpu'},
        {'model': 'self', 'field': 'motherboard'},
        {'model': 'self', 'field': 'ram'},
        {'model': 'self', 'field': 'gpu'},
        {'model': 'self', 'field': 'license_sticker'},
        {'model': 'self', 'field': 'power_supply'},
        {'model': 'self', 'field': 'description'},
    ]
    app_name = 'computer'
    button = Button(True, 'Добавить системый блок', 'admin:element_computer_add')


class CableAllView(TableView):
    """
    Класс представления, отвечающий за вывод таблицы с кабелем
    """
    model = models.Cable
    model_fields = [
        {'model': 'self', 'field': 'id', 'url': True},
        {'model': 'self', 'field': 'type'},
        {'model': 'self', 'field': 'length'},
        {'model': 'self', 'field': 'date'},
        {'model': 'self', 'field': 'description'},
    ]
    app_name = 'cable'
    button = Button(True, 'Добавить кабель', 'admin:element_cable_add')


class PaperView(ElementView):
    """
    Класс представления, отвечающий за вывод подробной информации о бумаге
    """
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
    """
    Класс представления, отвечающий за вывод подробной информации о дистрибутиве
    """
    model = models.Distribution
    model_fields = [
        {'model': 'self', 'field': 'name'},
        {'model': 'self', 'field': 'space'},
        {'model': 'self', 'field': 'count'},
        {'model': 'self', 'field': 'is_active'},
        {'model': 'self', 'field': 'description'},
    ]


class ComputerView(ElementView):
    """
    Класс представления, отвечающий за вывод подробной информации о системном блоке
    """
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


# TODO: Добавить авторизацию
class ComputerAPICreateView(View):
    """
    Класс представления, отвечающий за добавление компьютеров.
    Написан специально для скрипта инвентаризации ПК.
    Принимает данные через POST и добавляет новый пк.
    """

    def post(self, request, *args, **kwargs):
        from django.http import HttpResponse

        computer = models.Computer()
        space = request.POST.get('space', False)
        if space:
            computer.space_id = space
            computer.cpu = request.POST.get('cpu', '')
            computer.motherboard = request.POST.get('motherboard', '')
            computer.ram = request.POST.get('ram', '')
            computer.gpu = request.POST.get('gpu', '')
            computer.lan = ''
            computer.power_supply = ''
            computer.hdd = request.POST.get('hdd', '')
            computer.os = ''
            computer.description = request.POST.get('description', '')

            computer.save()

            return HttpResponse('Ok')
        else:
            return HttpResponse('Error')


class CableView(ElementView):
    """
    Класс представления, отвечающий за вывод подробной информации о кабеле
    """
    model = models.Cable
    model_fields = [
        {'model': 'self', 'field': 'space'},
        {'model': 'self', 'field': 'type'},
        {'model': 'self', 'field': 'length'},
        {'model': 'self', 'field': 'date'},
        {'model': 'self', 'field': 'is_active'},
        {'model': 'self', 'field': 'description'},
    ]
    template_name = 'element/cable.html'


class PaperMinusView(ElementMinusView):
    """
    Класс представления, отвечающий за уменьшение количества бумаги на складе
    """
    model = models.Paper


class DistributionMinusView(ElementMinusView):
    """
    Класс представления, отвечающий за уменьшение количества дистрибутивов на складе
    """
    model = models.Distribution
