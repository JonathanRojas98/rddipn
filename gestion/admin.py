from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(SubUnit)
class SubUnitAdmin(admin.ModelAdmin):
    list_display = (
        "order",
        "name",
        "order_as_str",
        "parent",
    )


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = (
        "order",
        "name",
        "goal",
    )


@admin.register(UnitResource)
class UnitResourceAdmin(admin.ModelAdmin):
    list_display = ("order", "name", "subtitle")


@admin.register(Glossary)
class GlossaryAdmin(admin.ModelAdmin):
    list_display = ("term",)


@admin.register(InfoResource)
class InfoResourceAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(SelfAssesmentResource)
class SelfAssesmentResourceAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(ActivityResource)
class ActivityResourceAdmin(admin.ModelAdmin):
    list_display = ("name",)
