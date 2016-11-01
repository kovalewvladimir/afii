from django.db import models
from django.shortcuts import get_object_or_404
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.urls import reverse

from element.field import Field, Element
from inventory.utils import get_status


# TODO: сделать вывод url
# TODO: реализовать вывод (да,нет) у полей BooleanField
class ElementManager(models.Manager):
    def get_element(self, pk, model_fields):
        element_db = get_object_or_404(self, pk=pk)
        model_meta = self.model._meta

        is_status = False
        if 'count' in model_fields and 'min_count' in model_fields:
            is_status = True

        fields = list()

        for mf in model_fields:
            field = Field()
            field.name = model_meta.get_field(mf).verbose_name.capitalize()
            field.value = getattr(element_db, 'get_%s_display' % mf, getattr(element_db, mf))
            if is_status and mf == 'count':
                field.status = get_status(element_db.count, element_db.min_count)
            fields.append(field)

        element = Element()
        element.name = str(element_db).capitalize()
        element.type_element = model_meta.verbose_name
        element.fields = fields
        element.link_to_image = element_db.image.url if element_db.image else static('inventory/img/default.png')
        element.link_to_page_edit = reverse('admin:%s_%s_change' % (model_meta.app_label, model_meta.model_name), args=(pk,))

        return element

