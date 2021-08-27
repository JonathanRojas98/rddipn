# Generated by Django 3.2.6 on 2021-08-27 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gestion", "0004_unit_header_color"),
    ]

    operations = [
        migrations.AddField(
            model_name="subunit",
            name="keywords",
            field=models.TextField(
                blank=True, help_text="Palabras clave (opcionales).", max_length=1000, null=True
            ),
        ),
    ]
