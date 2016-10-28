from django.contrib import admin
from space.models import Space


@admin.register(Space)
class SpaceAdmin(admin.ModelAdmin):
    pass
