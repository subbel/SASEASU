# Generated by Django 5.1.3 on 2025-04-18 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0016_alter_event_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='GBM',
        ),
        migrations.RemoveField(
            model_name='student',
            name='Industry',
        ),
        migrations.RemoveField(
            model_name='student',
            name='Socials',
        ),
    ]
