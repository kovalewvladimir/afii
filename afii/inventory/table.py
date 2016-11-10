# table = Table()
# table.header += [
#     '1',
#     '2',
# ]
# table.rows += [
#     Rows(Cell('name1', status='success'), Cell('name1'), category=1),
#     Rows(Cell('name2'), Cell('name1'), category=2),
#     Rows(Cell('name3'), Cell('name1', url='ad')),
#     Rows(Cell(items=[Items('asd', ' '), Items('asd2')]), Cell('name1'), category=4),
#     Rows(Cell('name5'), Cell('name1'), category=5),
# ]
from django.urls import NoReverseMatch
from django.urls import reverse

from inventory.utils import get_status_table


class Item:
    def __init__(self, name, url=None):
        self.name = name
        self.url = url


class Cell(Item):
    def __init__(self, name=None, url=None, status=None, items=None):
        super().__init__(name, url)
        self.status = status
        self.items = items


class Rows:
    def __init__(self, cell, category=None):
        self.cell = cell
        self.category = category


class Button:
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
    def __init__(self, table_id='table', button=Button()):
        self.header = list()
        self.rows = list()
        self.count = 0

        self.table_id = table_id
        self.button = button

    def append_row(self, cell, category=None):
        self.rows.append(Rows(cell, category))

    def get_status(self):
        status = 'success'
        for r in self.rows:
            for c in r.cell:
                status = get_status_table(status, c.status)
        return status

    def __iadd__(self, other):
        self.rows += other.rows
        self.header = other.header
        return self
