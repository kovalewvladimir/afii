class ListCategory(list):
    def get_all_count(self):
        count = 0
        for sc in self:
            count += sc.get_count()
        return count


class Category:
    def __init__(self, name=None):
        self.name = name
        self.sub_category = list()

    def get_count(self):
        count = 0
        for sc in self.sub_category:
            count += sc.count
        return count


class SubCategory:
    def __init__(self, name=None, category_id=None, count=0):
        self.name = name
        self.category_id = category_id
        self.count = count
