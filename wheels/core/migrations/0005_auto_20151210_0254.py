# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20151210_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='start',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
