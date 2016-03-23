# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='addr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address_1', models.CharField(max_length=128)),
                ('address_2', models.CharField(max_length=128, blank=True)),
                ('city', models.CharField(max_length=64)),
                ('state', models.CharField(max_length=64)),
                ('pin_code', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='bike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bikemodel', models.CharField(max_length=30, choices=[(b'Fire Z1', b'Fifox Z1'), (b'BT Zen', b'BTWin Zen')])),
                ('size', models.CharField(max_length=1, choices=[(b'S', b'Small'), (b'M', b'Medium'), (b'L', b'Large')])),
                ('date_deployed', models.DateField()),
                ('date_inspected', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_type', models.CharField(max_length=3, choices=[(b'PAN', b'PAN Card'), (b'ADH', b'Adhar Card')])),
                ('id_number', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('contact_num', models.CharField(max_length=10)),
                ('address', models.ForeignKey(to='core.addr')),
            ],
        ),
        migrations.CreateModel(
            name='station',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('x_coordinate', models.FloatField(null=True, blank=True)),
                ('y_coordinate', models.FloatField(null=True, blank=True)),
                ('address', models.ForeignKey(to='core.addr')),
            ],
        ),
        migrations.CreateModel(
            name='transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField(blank=True)),
                ('x_coordinate', models.FloatField(null=True, blank=True)),
                ('y_coordinate', models.FloatField(null=True, blank=True)),
                ('bike', models.ForeignKey(to='core.bike')),
                ('customer', models.ForeignKey(to='core.customer')),
                ('end_stn', models.ForeignKey(to='core.station', blank=True)),
                ('start_stn', models.ForeignKey(related_name='Start_Station', to='core.station')),
            ],
        ),
    ]
