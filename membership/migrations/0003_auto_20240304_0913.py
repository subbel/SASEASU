# Generated by Django 2.1.5 on 2024-03-04 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0002_student_payment_bool'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='GBM',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='Industry',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='Socials',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.CharField(default='Shang-Chi', max_length=120),
        ),
    ]