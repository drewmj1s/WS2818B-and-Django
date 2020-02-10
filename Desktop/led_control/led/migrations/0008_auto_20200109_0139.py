# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-09 01:39
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('led', '0007_auto_20200109_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pattern',
            name='speed_var',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
