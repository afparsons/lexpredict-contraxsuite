# Generated by Django 2.2.13 on 2020-12-08 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0069_auto_20201208_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='bad_health_check_num',
            field=models.IntegerField(default=0),
        ),
    ]