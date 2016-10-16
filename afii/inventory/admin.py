from django.contrib import admin
from inventory import models

admin.site.register(models.Space)
admin.site.register(models.Storage)
admin.site.register(models.BasePrinter)
admin.site.register(models.BaseCartridge)
admin.site.register(models.BaseZip)
admin.site.register(models.Cartridge)
admin.site.register(models.Printer)
admin.site.register(models.Zip)
admin.site.register(models.Paper)
admin.site.register(models.Computer)
admin.site.register(models.Distribution)
admin.site.register(models.Category)
admin.site.register(models.ItemStorage)
#admin.site.register(models.)