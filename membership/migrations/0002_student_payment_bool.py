# Generated by Django 2.1.5 on 2024-03-04 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='payment_bool',
            field=models.BooleanField(default=False),
        ),
    ]
