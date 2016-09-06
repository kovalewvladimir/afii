from django.contrib import admin
from inventory import models

admin.site.register(models.Space)
admin.site.register(models.Storage)
admin.site.register(models.BaseCartridge)
admin.site.register(models.BasePrinter)
admin.site.register(models.PaperSize)
admin.site.register(models.Cartridge)
admin.site.register(models.Printer)
#admin.site.register(models.)