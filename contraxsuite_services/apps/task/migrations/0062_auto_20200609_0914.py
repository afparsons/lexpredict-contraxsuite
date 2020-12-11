# Generated by Django 2.2.10 on 2020-06-09 09:14

from django.db import migrations


def run_migration(apps, schema_editor):
    # Deleting task config and app var for them to be restored with the default parameters.

    TaskConfig = apps.get_model('task', 'TaskConfig')
    TaskConfig.objects.filter(name='apps.task.tasks.create_document').delete()

    AppVar = apps.get_model('common', 'AppVar')
    AppVar.objects.filter(category='Document', name='tika_timeout').delete()


def revert_migration(apps, schema_editor):
    # Unfortunately this migration can not be reverted. There is no place to backup the previous task config params.
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('task', '0061_auto_20200424_1341'),
    ]

    operations = [
        migrations.RunPython(run_migration, reverse_code=revert_migration)
    ]