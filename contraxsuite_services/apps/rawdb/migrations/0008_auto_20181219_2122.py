# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-12-19 21:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rawdb', '0007_auto_20181219_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedfilter',
            name='title',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
