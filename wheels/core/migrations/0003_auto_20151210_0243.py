# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20151210_0238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='date_inspected',
            field=models.DateField(null=True, blank=True),
        ),
    ]
