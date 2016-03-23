# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20151210_0243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 9, 21, 23, 50, 461675, tzinfo=utc)),
        ),
    ]
