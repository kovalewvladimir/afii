from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from inventory.table import Button
from space import models


class TableView(ListView):
    model = None
    template_name = 'space/base_table.html'
    context_object_name = 'table'
    app_name = None
    model_fields = None
    button = Button()

    def get_queryset(self):
        return self.model.objects.get_table(int(self.args[0]), self.model_fields, self.button)

    def get_context_data(self, **kwargs):
        context = super(TableView, self).get_context_data(**kwargs)
        context['app_name'] = self.app_name
        context['space'] = get_object_or_404(models.Space, pk=int(self.args[0]))
        return context
