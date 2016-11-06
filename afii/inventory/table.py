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
    def __init__(self, *cell, category=None):
        self.cell = cell
        self.category = category


class Table:
    def __init__(self, table_id='table', is_button_add=True):
        self.header = list()
        self.rows = list()

        self.table_id = table_id
        self.is_button_add = is_button_add

    def append_row(self, *cell, category=None):
        self.rows.append(Rows(*cell, category))
