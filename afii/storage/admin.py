from django.contrib import admin
from storage.models import Storage, Category, ItemStorage


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('name', 'space',)
    list_filter = ('space',)
    list_select_related = True
    search_fields = ['name']

    radio_fields = {'space': admin.VERTICAL}


class CategoryInline(admin.TabularInline):
    model = Category
    extra = 0
    show_change_link = True


class ItemStorageInline(admin.StackedInline):
    model = ItemStorage
    extra = 0
    show_change_link = True


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ordering = ('base_category',)
    list_display = ('name', 'storage', 'is_base', 'base_category',)
    list_filter = ('storage', 'is_base', 'base_category',)
    list_select_related = True
    search_fields = ['name']

    inlines = [CategoryInline, ItemStorageInline]
    raw_id_fields = ('base_category',)
    radio_fields = {'storage': admin.VERTICAL}


@admin.register(ItemStorage)
class ItemStorageAdmin(admin.ModelAdmin):
    ordering = ('category',)
    list_display = ('name', 'category', 'is_active')
    list_filter = ('category', 'is_active',)
    list_select_related = True
    search_fields = ['name']

    raw_id_fields = ('category',)
