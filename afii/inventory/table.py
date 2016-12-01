from django.urls import NoReverseMatch
from django.urls import reverse

from inventory.utils import get_status_table


class Item:
    """
    В ячейке таблицы может быть несколько полей, для агрегации этих полей используется этот класс
    """
    def __init__(self, name, url=None):
        self.name = name
        self.url = url


class Cell(Item):
    """
    Класс описывает ячейки таблицы
    """
    def __init__(self, name=None, url=None, status=None, items=None):
        super().__init__(name, url)
        self.status = status
        self.items = items


class Rows:
    """
    Класс описывает строки таблицы
    """
    def __init__(self, cell, category=None):
        self.cell = cell
        self.category = category


class Button:
    """
    Класс описывает кнопку добавления/редактирования элементов таблицы
    """
    def __init__(self, is_button=False, button_name=None, button_url=None):
        self.is_button = is_button
        self.button_name = button_name
        self.button_url = button_url

    def get_absolute_url(self):
        try:
            return reverse(self.button_url)
        except NoReverseMatch:
            return None


class Table:
    """
    Класс описывает таблицу. Состоит из строк (класс Rows),
    заголовка таблицы, кол-ва элементов таблицы, идентификатора таблицы,
    кнопки добавления/редактирования элементов таблицы;
    """
    def __init__(self, table_id='table', button=Button()):
        self.header = list()
        self.rows = list()
        self.count = 0

        self.table_id = table_id
        self.button = button

    def append_row(self, cell, category=None):
        """
        Создает строку из списка ячеек
        :param cell: список ячеек
        :param category: id категории строки, используется для склада
        :return: ничего не возвращает
        """
        self.rows.append(Rows(cell, category))

    def get_status(self):
        """
        Получает статус таблицы
        """
        status = 'success'
        for r in self.rows:
            for c in r.cell:
                status = get_status_table(status, c.status)
        return status

    def __iadd__(self, other):
        """
        Перегрузил оператор +=
        """
        self.rows += other.rows
        self.header = other.header
        return self
