# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20151210_0254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='end_stn',
            field=models.ForeignKey(blank=True, to='core.station', null=True),
        ),
    ]
