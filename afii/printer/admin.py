from django.contrib import admin
from printer.models import BasePrinter, BaseCartridge, BaseZip, Printer, Cartridge, Zip


class BasePrinterInline(admin.StackedInline):
    model = Printer
    extra = 0
    show_change_link = True


@admin.register(BasePrinter)
class BasePrinterAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('name', 'type_printing', 'type')
    list_filter = ('type_printing', 'type')
    search_fields = ['name']

    inlines = [BasePrinterInline]
    radio_fields = {'type_printing': admin.VERTICAL,
                    'type': admin.VERTICAL,
                    'color': admin.VERTICAL,
                    'type_paper': admin.HORIZONTAL}


class BaseCartridgeInline(admin.StackedInline):
    model = Cartridge
    extra = 0
    show_change_link = True


@admin.register(BaseCartridge)
class BaseCartridgeAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('name', 'type', 'recycling')
    list_filter = ('type', 'recycling')
    search_fields = ['name']

    inlines = [BaseCartridgeInline]
    filter_horizontal = ('base_printers',)
    radio_fields = {'type': admin.VERTICAL,
                    'color': admin.VERTICAL}


class BaseZipInline(admin.StackedInline):
    model = Zip
    extra = 0
    show_change_link = True


@admin.register(BaseZip)
class BaseZipAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('name', 'type')
    list_filter = ('type',)
    search_fields = ['name']

    inlines = [BaseZipInline]
    filter_horizontal = ('base_printers',)


@admin.register(Printer)
class PrinterAdmin(admin.ModelAdmin):
    ordering = ('base_printer',)
    list_display = ('base_printer', 'space', 'cabinet', 'is_active')
    list_filter = ('space', 'is_active')
    list_select_related = True
    search_fields = ['base_printer__name', 'space__name']

    raw_id_fields = ('base_printer',)
    radio_fields = {'space': admin.VERTICAL}


@admin.register(Cartridge)
class CartridgeAdmin(admin.ModelAdmin):
    ordering = ('base_cartridge',)
    list_display = ('base_cartridge', 'space', 'is_active')
    list_filter = ('space', 'is_active')
    list_select_related = True
    search_fields = ['base_cartridge__name', 'space__name']

    raw_id_fields = ('base_cartridge',)
    radio_fields = {'space': admin.VERTICAL}


@admin.register(Zip)
class ZipAdmin(admin.ModelAdmin):
    ordering = ('base_zip',)
    list_display = ('base_zip', 'space', 'is_active')
    list_filter = ('space', 'is_active')
    list_select_related = True
    search_fields = ['base_zip__name', 'space__name']

    raw_id_fields = ('base_zip',)
    radio_fields = {'space': admin.VERTICAL}
