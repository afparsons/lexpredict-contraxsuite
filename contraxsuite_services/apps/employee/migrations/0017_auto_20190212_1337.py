# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-02-12 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0016_employee_has_severance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employerusage',
            name='count',
            field=models.IntegerField(db_index=True, default=0),
        ),
    ]