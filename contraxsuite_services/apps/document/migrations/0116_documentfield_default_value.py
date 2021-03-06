# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-01-16 17:46
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
import django.core.serializers.json
from django.db import migrations
from apps.common.model_utils.improved_django_json_encoder import ImprovedDjangoJSONEncoder


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0115_auto_20190116_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentfield',
            name='default_value',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, encoder=ImprovedDjangoJSONEncoder, null=True),
        ),
    ]
