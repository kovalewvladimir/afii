from django.db import models
from django.urls import reverse

from inventory.table import Table, Rows, Cell
from inventory.utils import get_data, get_field_display, get_is_count_status, get_status


class TableManager(models.Manager):
    """
    Менеджер применим к моделям, которые могут формировать таблицы
    """
    def _filter_data(self, space_id):
        """
        Фильтрует модель по полю  is_active=True и space__pk=space_id.
        При желании метод можно перегрузить
        :param space_id: id площадки
        :return: модель после фильтрации данных
        """
        data = self.select_related()
        data = data.filter(is_active=True)
        data = data.filter(space__pk=space_id)
        return data

    def get_table(self, space_id, model_fields=None, button=None, is_category=False):
        """
        Формирует таблицу (класс Table) из модели
        :param space_id: id площадки
        :param model_fields: словарь с полями модели
        :param button: кнопка редактирования
        :param is_category: добавлять к строке атрибут category
        :return: таблица, экземпляр класса Table
        """
        data = self._filter_data(space_id)

        table = Table()
        table.button = button

        is_count_status = get_is_count_status(model_fields)

        is_header = True
        for d in data:
            cells = list()
            for mf in model_fields:
                m = mf['model']
                f = mf['field']
                u = mf.get('url')
                _d = get_data(m, d)

                if is_header:
                    table.header.append(d.get_field(f))

                cell = Cell()
                if is_count_status and f == 'count':
                    cell.status = get_status(_d.count, _d.min_count)
                if u:
                    cell.url = _d.get_absolute_url()
                cell.name = get_field_display(_d, f)
                cells.append(cell)
            rows = Rows(cells)
            if is_category:
                rows.category = d.category.id
            table.rows.append(rows)
            is_header = False

        return table
