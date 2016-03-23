# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bike_model', models.CharField(max_length=200)),
                ('depl_date', models.DateTimeField(verbose_name=b'Date Deployed')),
                ('position_x', models.FloatField()),
                ('position_y', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('pan_id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('mem_join', models.DateTimeField(verbose_name=b'Date Joined')),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coordinates_x', models.FloatField()),
                ('coordinates_y', models.FloatField()),
                ('Incharge', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('rate', models.IntegerField(default=10)),
                ('bike', models.ForeignKey(to='core.Bike')),
                ('cust', models.ForeignKey(to='core.Customer')),
            ],
        ),
    ]
