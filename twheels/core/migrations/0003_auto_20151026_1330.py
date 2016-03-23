# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20151022_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='name',
            field=models.CharField(default=b'Name', max_length=100),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='end_time',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
