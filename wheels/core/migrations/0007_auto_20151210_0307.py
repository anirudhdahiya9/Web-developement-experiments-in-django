# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20151210_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='end',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
