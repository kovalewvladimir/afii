from django.db import models

from element.managers import ElementAndTableManager
from storage.category import ListCategory, Category, SubCategory


class ItemStorageManager(ElementAndTableManager):
    def _filter_data(self, storage_id):
        data = self
        data = data.select_related()
        data = data.filter(is_active=True)
        data = data.filter(category__storage__id=storage_id)
        return data


class CategoryManager(models.Manager):
    def get_category(self, storage_id):
        c_db = self
        c_db = c_db.select_related()
        c_db = c_db.prefetch_related('categories__items')
        c_db = c_db.filter(is_base=True)
        c_db = c_db.filter(storage__pk=storage_id)

        list_category = ListCategory()
        for c in c_db:
            category = Category(c.name, c.pk)
            for i in c.categories.all():
                sub_category = SubCategory()
                sub_category.name = i.name
                sub_category.category_id = i.pk
                sub_category.count = i.items.count()
                category.sub_category.append(sub_category)
            list_category.append(category)

        return list_category
