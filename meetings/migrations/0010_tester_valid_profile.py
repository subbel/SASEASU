# Generated by Django 5.1.3 on 2025-01-19 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0009_student_valid_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='tester',
            name='valid_profile',
            field=models.BooleanField(default=False),
        ),
    ]
