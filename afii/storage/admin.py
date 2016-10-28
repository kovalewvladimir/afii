from django.contrib import admin
from storage.models import Storage


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    pass
