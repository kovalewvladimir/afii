from django.shortcuts import get_object_or_404

from element.views import ElementView, ElementMinusView
from inventory.views import TableView
from storage import models


class StorageView(TableView):
    """
    Класс представления, отвечающий за вывод таблицы товар
    (единица складского учета). В классе перегружен метод
    get_context_data базового класса
    """
    model = models.ItemStorage
    model_fields = [
        {'model': 'self', 'field': 'id'},
        {'model': 'self', 'field': 'name', 'url': True},
        {'model': 'self', 'field': 'shelf'},
        {'model': 'self', 'field': 'count'},
    ]
    is_category = True
    template_name = 'storage/storage.html'

    def get_context_data(self, **kwargs):
        category_id = int(self.args[0])
        context = super(TableView, self).get_context_data(**kwargs)
        context['storage'] = get_object_or_404(models.Storage.objects.select_related('space'), pk=category_id)
        context['space'] = context['storage'].space
        context['category'] = models.Category.objects.get_category(category_id)
        return context


class ItemStorageView(ElementView):
    """
    Класс представления, отвечающий за вывод подробной
    информации о товаре (единица складского учета)
    """
    model = models.ItemStorage
    model_fields = [
        {'model': 'self', 'field': 'name'},
        {'model': 'self', 'field': 'category'},
        {'model': 'self', 'field': 'count'},
        {'model': 'self', 'field': 'shelf'},
        {'model': 'self', 'field': 'is_active'},
        {'model': 'self', 'field': 'description'},
    ]


class ItemStorageMinusView(ElementMinusView):
    """
    Класс представления, отвечающий за уменьшение количества
    товара (единица складского учета) на складе
    """
    model = models.ItemStorage
