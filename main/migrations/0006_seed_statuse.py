from django.db import migrations
from ..config import column_names


def create_statuses(apps, schema_editor):
    Status = apps.get_model('main', 'Status')
    for status in column_names:
        Status.objects.create(name_status=status)


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_task_deadline'),
    ]

    operations = [
        migrations.RunPython(create_statuses),
    ]
