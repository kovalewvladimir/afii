from django.db import models
from django.shortcuts import get_object_or_404
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.urls import reverse

from element.field import Field, Element
from inventory.utils import get_status


# TODO: сделать вывод url
# TODO: реализовать вывод (да,нет) у полей BooleanField
class ElementManager(models.Manager):
    element_db = None

    def get_element(self, pk, model_fields):
        element_db = get_object_or_404(self, pk=pk)

        is_count = False
        is_min_count = False
        for mf in model_fields:
            if mf['field'] == 'count':
                is_count = True
            if mf['field'] == 'min_count':
                is_min_count = True
        is_status = is_count and is_min_count

        fields = list()

        for mf in model_fields:
            m = mf['model']
            f = mf['field']
            if mf['model'] == 'self':
                e_db = element_db
            else:
                e_db = getattr(element_db, m)
            field = Field()
            field.name = e_db.get_field(f)
            field.value = getattr(e_db, 'get_%s_display' % f, getattr(e_db, f))
            if is_status and f == 'count':
                field.status = get_status(e_db.count, e_db.min_count)
            fields.append(field)

        element = Element()
        element.name = str(element_db).capitalize()
        element.type_element = element_db.get_verbose_name
        element.fields = fields
        element.link_to_image = element_db.image.url if element_db.image else static('inventory/img/default.png')
        element.link_to_page_edit = element_db.get_admin_change_edit()

        self.element_db = element_db
        return element
