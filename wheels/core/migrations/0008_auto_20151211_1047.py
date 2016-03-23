# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20151210_0307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='x_coordinate',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='y_coordinate',
        ),
        migrations.AddField(
            model_name='bike',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='bike',
            name='x_coordinate',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bike',
            name='y_coordinate',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
