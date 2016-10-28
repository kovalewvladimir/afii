from django.contrib import admin
from storage.models import Storage


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('name', 'space',)
    list_filter = ('space',)
    search_fields = ['name']

    radio_fields = {'space': admin.VERTICAL}
