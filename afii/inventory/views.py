from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from inventory.table import Button
from space import models


@method_decorator(login_required, name='dispatch')
class TableView(ListView):
    """
    Класс представления используется для отображения модели,
    которая реализует менеджер TableManager.
    Атрибуты:
        model – модель для вывода;
        model_fields – поля модели для вывода;
        template_name – шаблон для отображения;
        context_object_name – имя таблицы, передаваемое в шаблон;
        app_name – имя модуля;
        button – кнопка добавления/редактирования элементов таблицы;
        is_category – добавлять ли атрибут категория в строки таблицы;
    """
    model = None
    model_fields = None
    template_name = 'space/base_table.html'
    context_object_name = 'table'
    app_name = None
    button = Button()
    is_category = False

    def get_queryset(self):
        """
        Возвращает объект queryset, который буден использован для получения
        объекта для данного представления. По умолчанию, метод get_queryset()
        возвращает значение атрибута queryset (если он установлен), - в
        противном случае будет создан экземпляр класса QuerySet вызовом
        метода all() у атрибута :attr:`model`( с помощью менеджера по умолчанию).
        :return: таблицу класс Table
        """
        return self.model.objects.get_table(int(self.args[0]), self.model_fields, self.button, self.is_category)

    def get_context_data(self, **kwargs):
        """
        Возвращает данные контекста для отображения списка объектов.
        Встроенная реализация этого метода требует чтобы атрибут self.object
        был установлен в представлении (пускай даже в None). Не забудьте об этом,
        когда будете использовать этот mixin без одного из встроенных представлений,
        которое уже делает это.
        Возвращает словарь со следующим содержимым:
            object: Объект, который отображается представлением (self.object).
            context_object_name: self.object будет сохранен в контексте под
            именем, которое вернул метод get_context_object_name(). По умолчанию
            это название модели в нижнем регистре.
        """
        context = super(TableView, self).get_context_data(**kwargs)
        context['app_name'] = self.app_name
        context['space'] = get_object_or_404(models.Space, pk=int(self.args[0]))
        return context

