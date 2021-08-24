from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = (
        "order",
        "name",
        "goal",
    )


@admin.register(SubUnit)
class SubUnitAdmin(admin.ModelAdmin):
    list_display = (
        "parent",
        "order",
        "order_as_str",
        "name",
    )
