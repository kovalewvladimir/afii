from django.contrib import admin
from printer.models import BasePrinter, BaseCartridge, BaseZip, Printer, Cartridge, Zip


@admin.register(BasePrinter)
class BasePrinterAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('name', 'type_printing', 'type')
    list_filter = ('type_printing', 'type')

    radio_fields = {'type_printing': admin.VERTICAL,
                    'type': admin.VERTICAL,
                    'color': admin.VERTICAL,
                    'type_paper': admin.HORIZONTAL}


@admin.register(BaseCartridge)
class BaseCartridgeAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('name', 'type', 'recycling')
    list_filter = ('type', 'recycling')

    filter_vertical = ('base_printers',)
    radio_fields = {'type': admin.VERTICAL,
                    'color': admin.VERTICAL}


@admin.register(BaseZip)
class BaseZipAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('name', 'type')
    list_filter = ('type',)

    filter_vertical = ('base_printers',)


@admin.register(Printer)
class PrinterAdmin(admin.ModelAdmin):
    ordering = ('base_printer',)
    list_display = ('base_printer', 'space', 'cabinet', 'delete')
    list_filter = ('space', 'delete')
    list_select_related = True

    raw_id_fields = ('base_printer',)
    radio_fields = {'space': admin.VERTICAL}


@admin.register(Cartridge)
class CartridgeAdmin(admin.ModelAdmin):
    ordering = ('base_cartridge',)
    list_display = ('base_cartridge', 'space', 'delete')
    list_filter = ('space', 'delete')
    list_select_related = True

    raw_id_fields = ('base_cartridge',)
    radio_fields = {'space': admin.VERTICAL}


@admin.register(Zip)
class ZipAdmin(admin.ModelAdmin):
    ordering = ('base_zip',)
    list_display = ('base_zip', 'space', 'delete')
    list_filter = ('space', 'delete')
    list_select_related = True

    raw_id_fields = ('base_zip',)
    radio_fields = {'space': admin.VERTICAL}