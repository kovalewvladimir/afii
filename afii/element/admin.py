from django.contrib import admin
from element.models import Paper, Distribution, Computer


@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('name', 'space', 'type_paper', 'is_active')
    list_filter = ('space', 'type_paper')
    search_fields = ['name']

    radio_fields = {'space': admin.VERTICAL,
                    'type_paper': admin.HORIZONTAL}


@admin.register(Distribution)
class DistributionAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('name', 'space', 'is_active')
    list_filter = ('space',)
    search_fields = ['name']

    radio_fields = {'space': admin.VERTICAL}


@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
    ordering = ('cpu',)
    list_display = ('cpu', 'motherboard', 'ram', 'space', 'is_active')
    list_filter = ('space',)
    search_fields = ['cpu']

    radio_fields = {'space': admin.VERTICAL}
