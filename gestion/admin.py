from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(SubUnit)
class SubUnitAdmin(admin.ModelAdmin):
    list_display = (
        "order",
        "parent",
        "order_as_str",
        "name",
    )


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = (
        "order",
        "name",
        "goal",
    )
