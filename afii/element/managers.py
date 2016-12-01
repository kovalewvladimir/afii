from django.db import models
from django.shortcuts import get_object_or_404
from django.contrib.staticfiles.templatetags.staticfiles import static


from element.field import Field, Element
from inventory.managers import TableManager
from inventory.utils import get_status, get_is_count_status, get_data, get_field_display


# TODO: реализовать вывод (да,нет) у полей BooleanField
class ElementManager(models.Manager):
    """
    Менеджер применим к моделям, которые могут формировать
    элементы (класс Element)
    """
    element_db = None

    def get_element(self, pk, model_fields):
        """
        Формирует элемент
        """
        db = self.select_related()
        element_db = get_object_or_404(db, pk=pk)

        is_count_status = get_is_count_status(model_fields)
        fields = list()

        for mf in model_fields:
            m = mf['model']
            f = mf['field']
            u = mf.get('url')
            e_db = get_data(m, element_db)
            field = Field()
            field.name = e_db.get_field(f)
            field.value = get_field_display(e_db, f)
            if is_count_status and f == 'count':
                field.status = get_status(e_db.count, e_db.min_count)
            if u:
                field.url = 'http://' + field.value
            fields.append(field)

        element = Element()
        element.name = str(element_db)
        element.type_element = element_db.get_verbose_name
        element.fields = fields
        element.link_to_image = element_db.image.url if element_db.image else static('inventory/img/default.png')
        element.link_to_page_edit = element_db.get_admin_change_edit()

        self.element_db = element_db
        return element


class ElementAndTableManager(ElementManager, TableManager):
    """
    Менеджер применим к моделям, которые могут формировать
    элементы (класс Element) и таблицы (класс Table)
    """
    pass
