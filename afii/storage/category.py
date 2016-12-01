class ListCategory(list):
    """
    Класс, описывающий список категорий
    """
    def get_all_count(self):
        """
        Подсчитывает общее кол-во товара в списке категорий
        :return: кол-во товара
        """
        count = 0
        for sc in self:
            count += sc.get_count()
        return count


class Category:
    """
    Класс, описывающий категорию
    """
    def __init__(self, name=None):
        self.name = name
        self.sub_category = list()

    def get_count(self):
        """
        Подсчитывает кол-во товара в категории
        :return: кол-во товара
        """
        count = 0
        for sc in self.sub_category:
            count += sc.count
        return count


class SubCategory:
    """
    Класс, описывающий под категорию
    """
    def __init__(self, name=None, category_id=None, count=0):
        self.name = name
        self.category_id = category_id
        self.count = count
