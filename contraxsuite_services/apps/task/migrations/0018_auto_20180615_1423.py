# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-06-15 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0017_auto_20180615_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='duration_at_last_update_time',
            field=models.DurationField(blank=True, null=True),
        ),
    ]