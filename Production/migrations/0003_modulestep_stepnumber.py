# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-24 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Production', '0002_auto_20180419_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='modulestep',
            name='StepNumber',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]