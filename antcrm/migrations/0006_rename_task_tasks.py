# Generated by Django 4.2.6 on 2023-10-18 04:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('antcrm', '0005_task'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Task',
            new_name='Tasks',
        ),
    ]
