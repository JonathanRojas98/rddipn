# Generated by Django 3.2.6 on 2021-08-24 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_auto_20210824_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subunit',
            name='name',
            field=models.CharField(help_text='Nombre de la unidad.', max_length=50, verbose_name='Nombre de la unidad'),
        ),
        migrations.AlterField(
            model_name='subunit',
            name='order',
            field=models.PositiveIntegerField(help_text='Índice de la unidad (usado para ordenar cada unidad).', unique=True, verbose_name='Índice'),
        ),
        migrations.AlterField(
            model_name='subunit',
            name='order_as_str',
            field=models.CharField(help_text='Índice a mostrar en el sitio (Ej: 1.2.3).', max_length=10, unique=True, verbose_name='Índice (temario)'),
        ),
        migrations.AlterField(
            model_name='subunit',
            name='parent',
            field=models.ForeignKey(help_text='Sección padre de esta subunidad.', on_delete=django.db.models.deletion.CASCADE, related_name='SubUnit', to='gestion.unit', verbose_name='Sección padre'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='goal',
            field=models.CharField(default='Ejemplo', help_text='Objetivo de la materia.', max_length=200, verbose_name='Objetivo'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='name',
            field=models.CharField(help_text='Nombre de la unidad.', max_length=50, verbose_name='Nombre de la unidad'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='order',
            field=models.PositiveIntegerField(help_text='Índice de la unidad (usado para ordenar cada unidad).', unique=True, verbose_name='Índice'),
        ),
    ]
