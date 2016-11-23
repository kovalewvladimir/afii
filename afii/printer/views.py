from django.http import Http404
from django.shortcuts import redirect, get_object_or_404, get_list_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View

from element.views import ElementView, ElementMinusView
from inventory.table import Button
from printer import models
from inventory.views import TableView


class PrinterAllView(TableView):
    model = models.Printer
    app_name = 'printer'
    button = Button(True, 'Добавить принтер', 'admin:printer_printer_add')


class CartridgeAllView(TableView):
    model = models.Cartridge
    app_name = 'cartridge'
    template_name = 'printer/cartridge_all.html'
    context_object_name = 'tables'


class ZipAllView(TableView):
    model = models.Zip
    app_name = 'zip'
    button = Button(True, 'Добавить ЗИП', 'admin:printer_zip_add')


class PrinterView(ElementView):
    model = models.Printer
    model_fields = [
        {'model': 'self', 'field': 'base_printer'},
        {'model': 'self', 'field': 'space'},
        {'model': 'self', 'field': 'cabinet'},
        {'model': 'self', 'field': 'user'},
        {'model': 'base_printer', 'field': 'type_printing'},
        {'model': 'base_printer', 'field': 'type'},
        {'model': 'base_printer', 'field': 'color'},
        {'model': 'base_printer', 'field': 'type_paper'},
        {'model': 'self', 'field': 'ip', 'url': True},
        {'model': 'self', 'field': 'login'},
        {'model': 'self', 'field': 'password'},
        {'model': 'self', 'field': 'sn'},
        {'model': 'self', 'field': 'date'},
        {'model': 'self', 'field': 'is_active'},
        {'model': 'base_printer', 'field': 'info_consumables', 'url': True},
        {'model': 'self', 'field': 'description'},
    ]
    template_name = 'printer/printer.html'


class CartridgeView(ElementView):
    model = models.Cartridge
    model_fields = [
        {'model': 'self', 'field': 'base_cartridge'},
        {'model': 'self', 'field': 'space'},
        {'model': 'self', 'field': 'shelf'},
        {'model': 'base_cartridge', 'field': 'type'},
        {'model': 'self', 'field': 'count', 'status': True},
        {'model': 'self', 'field': 'min_count'},
        {'model': 'self', 'field': 'is_active'},
        {'model': 'self', 'field': 'description'},
    ]
    template_name = 'printer/cartridge_or_zip.html'


class ZipView(ElementView):
    model = models.Zip
    model_fields = [
        {'model': 'self', 'field': 'base_zip'},
        {'model': 'base_zip', 'field': 'type'},
        {'model': 'self', 'field': 'space'},
        {'model': 'self', 'field': 'shelf'},
        {'model': 'self', 'field': 'count', 'status': True},
        {'model': 'self', 'field': 'min_count'},
        {'model': 'self', 'field': 'is_active'},
        {'model': 'self', 'field': 'description'},
    ]
    template_name = 'printer/cartridge_or_zip.html'


class CartridgeMinusView(ElementMinusView):
    model = models.Cartridge

    def post(self, request, *args, **kwargs):
        if self.model is None:
            raise Http404()
        cartridge = get_object_or_404(self.model, pk=int(args[0]))
        is_recycling = cartridge.base_cartridge.recycling
        cartridge.count -= 1
        if is_recycling:
            cartridge.count_recycling += 1
        if cartridge.count >= 0:
            cartridge.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))


class ZipMinusView(ElementMinusView):
    model = models.Zip


@method_decorator(login_required, name='dispatch')
class CartridgeSendToRecyclingView(View):
    def post(self, request, *args, **kwargs):
        cartridges = models.Cartridge.objects
        cartridges = cartridges.select_related()
        cartridges = cartridges.filter(space__pk=int(args[0]))
        cartridges = cartridges.filter(base_cartridge__recycling=True)
        cartridges = cartridges.filter(count_recycling__gt=0)

        for c in cartridges:
            c.count_in_recycling += c.count_recycling
            c.count_recycling = 0
            c.save()

        return redirect(request.META.get('HTTP_REFERER', '/'))

    def get(self, request, *args, **kwargs):
        raise Http404()


@method_decorator(login_required, name='dispatch')
class CartridgeInRecyclingView(View):
    def post(self, request, *args, **kwargs):
        cartridges = models.Cartridge.objects
        cartridges = cartridges.select_related()
        cartridges = cartridges.filter(space__pk=int(args[0]))
        cartridges = cartridges.filter(base_cartridge__recycling=True)
        cartridges = cartridges.filter(count_in_recycling__gt=0)

        for c in cartridges:
            c.count += c.count_in_recycling
            c.count_in_recycling = 0
            c.save()

        return redirect(request.META.get('HTTP_REFERER', '/'))

    def get(self, request, *args, **kwargs):
        raise Http404()
