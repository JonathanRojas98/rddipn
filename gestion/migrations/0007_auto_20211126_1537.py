# Generated by Django 3.2.6 on 2021-11-26 15:37

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ("gestion", "0006_alter_subunit_contents"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subunit",
            name="contents",
            field=tinymce.models.HTMLField(help_text="Contenidos de esta subunidad."),
        ),
        migrations.CreateModel(
            name="UnitResource",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Nombre de la unidad.",
                        max_length=50,
                        verbose_name="Nombre de la unidad",
                    ),
                ),
                (
                    "order",
                    models.PositiveIntegerField(
                        help_text="Índice de la unidad (usado para ordenar cada unidad).",
                        unique=True,
                        verbose_name="Índice",
                    ),
                ),
                (
                    "contents",
                    models.TextField(
                        help_text="Contenidos (HTML) para este recurso.",
                        max_length=1000,
                    ),
                ),
                (
                    "subtitle",
                    models.TextField(
                        blank=True,
                        help_text="Subtítulo, opcional.",
                        max_length=1000,
                        null=True,
                    ),
                ),
                (
                    "order_as_str",
                    models.CharField(
                        help_text="Índice a mostrar en el sitio (Ej: 1.2.3).",
                        max_length=10,
                        unique=True,
                        verbose_name="Índice (temario)",
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        help_text="Sección padre de este recurso.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ResourceUnit",
                        to="gestion.unit",
                        verbose_name="Sección padre",
                    ),
                ),
            ],
            options={
                "ordering": ("order",),
            },
        ),
    ]