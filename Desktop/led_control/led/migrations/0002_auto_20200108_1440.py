# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-08 14:40
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('led', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='strip',
            name='current_pattern',
        ),
        migrations.AddField(
            model_name='pattern',
            name='num_leds',
            field=models.IntegerField(default=150, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(150)]),
        ),
        migrations.AddField(
            model_name='pattern',
            name='speed_var',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.DeleteModel(
            name='Strip',
        ),
    ]