from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from element.views import ElementView, ElementMinusView
from inventory.views import TableView
from storage import models
from storage.forms import AddCategoryForm


class StorageView(TableView):
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

        context['add_category_form'] = AddCategoryForm

        return context


class ItemStorageView(ElementView):
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
    model = models.ItemStorage


@method_decorator(login_required, name='dispatch')
class AddCategoryView(View):
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = AddCategoryForm(request.POST)
            args = {'add_category_form': form}
            if form.is_valid():
                return render(request, 'storage/form_add_category.html', args)
            else:
                return render(request, 'storage/form_add_category.html', args)
        else:
            raise Http404()

    def get(self, request, *args, **kwargs):
        raise Http404()
