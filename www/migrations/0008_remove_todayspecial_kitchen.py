# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-07 18:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0007_todayspecial_kitchen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todayspecial',
            name='kitchen',
        ),
    ]
