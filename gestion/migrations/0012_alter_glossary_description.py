# Generated by Django 3.2.6 on 2022-04-04 03:43

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0011_auto_20220404_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glossary',
            name='description',
            field=tinymce.models.HTMLField(help_text='Descripción de este término.'),
        ),
    ]
