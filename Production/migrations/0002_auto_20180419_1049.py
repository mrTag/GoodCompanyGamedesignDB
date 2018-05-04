# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-19 08:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Production', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='material',
            options={'verbose_name': 'Material', 'verbose_name_plural': 'Materials'},
        ),
        migrations.AlterModelOptions(
            name='module',
            options={'verbose_name': 'Module', 'verbose_name_plural': 'Modules'},
        ),
        migrations.AlterModelOptions(
            name='moduleslottype',
            options={'verbose_name': 'Module Slot Type', 'verbose_name_plural': 'Module Slot Types'},
        ),
        migrations.AlterModelOptions(
            name='modulestep',
            options={'verbose_name': 'Module Step', 'verbose_name_plural': 'Module Steps'},
        ),
        migrations.AlterModelOptions(
            name='modulestepinputmaterialamount',
            options={'verbose_name': 'Input Material', 'verbose_name_plural': 'Input Materials'},
        ),
        migrations.AlterModelOptions(
            name='modulestepoutputmaterialamount',
            options={'verbose_name': 'Output Material', 'verbose_name_plural': 'Output Materials'},
        ),
        migrations.AlterModelOptions(
            name='producttype',
            options={'verbose_name': 'Product Type', 'verbose_name_plural': 'Product Types'},
        ),
        migrations.AlterField(
            model_name='module',
            name='FitsIntoSlot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FittingModule', to='Production.ModuleSlotType'),
        ),
        migrations.AlterField(
            model_name='producttype',
            name='Slots',
            field=models.ManyToManyField(related_name='UsedInProductType', to='Production.ModuleSlotType'),
        ),
    ]