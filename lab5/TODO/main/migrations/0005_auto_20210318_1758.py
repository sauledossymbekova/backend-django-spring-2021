# Generated by Django 3.1.7 on 2021-03-18 11:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210318_1743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='due_on',
        ),
        migrations.AddField(
            model_name='task',
            name='due',
            field=models.DateField(default=datetime.date(2021, 3, 20)),
        ),
    ]