from django.db import models


class BaseUnit(models.Model):
    """
    Base class with common attributes.
    """

    class Meta:
        abstract = True

    name = models.CharField(
        max_length=50, help_text="Nombre de la unidad.", verbose_name="Nombre de la unidad"
    )
    order = models.PositiveIntegerField(
        unique=True, help_text="Índice de la unidad (usado para ordenar cada unidad).", verbose_name="Índice"
    )


class Unit(BaseUnit):
    class Meta:
        ordering = ("order",)

    goal = models.CharField(
        max_length=200, default="Ejemplo", help_text="Objetivo de la materia.", verbose_name="Objetivo"
    )

    def __str__(self):
        return self.name


class SubUnit(BaseUnit):
    class Meta:
        ordering = ("order",)

    parent = models.ForeignKey(
        Unit,
        on_delete=models.CASCADE,
        related_name="SubUnit",
        help_text="Sección padre de esta subunidad.",
        verbose_name="Sección padre",
    )
    contents = models.TextField(max_length=100000, help_text="Contenidos (html).")
    order_as_str = models.CharField(
        max_length=10,
        unique=True,
        help_text="Índice a mostrar en el sitio (Ej: 1.2.3).",
        verbose_name="Índice (temario)",
    )

    def __str__(self):
        return f"{self.order_as_str}: {self.name}"