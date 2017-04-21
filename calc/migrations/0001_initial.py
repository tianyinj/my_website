# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 20:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(default=b'', max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('earnings_per_hr', models.FloatField()),
                ('trips_per_hr', models.FloatField()),
                ('earnings_per_mi', models.FloatField()),
                ('occupancy_rate', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=255)),
                ('beginshift_at', models.DateTimeField()),
                ('endshift_at', models.DateTimeField()),
                ('shift_cutoff', models.IntegerField(default=0)),
                ('shift_padding', models.IntegerField(default=0)),
                ('shift_trips', models.IntegerField(default=0)),
                ('shift_earn', models.FloatField(default=0)),
                ('shift_distance', models.FloatField(default=0)),
                ('shift_busy', models.FloatField(default=0)),
                ('shift_span', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_id', models.CharField(max_length=255)),
                ('user_id', models.CharField(max_length=255)),
                ('trip_type', models.CharField(max_length=255)),
                ('driver_id', models.IntegerField(default=0)),
                ('shift_id', models.IntegerField(default=0)),
                ('request_at', models.DateTimeField()),
                ('begintrip_at', models.DateTimeField()),
                ('dropoff_at', models.DateTimeField()),
                ('distance', models.FloatField()),
                ('duration', models.FloatField()),
                ('fare', models.FloatField()),
                ('surge', models.FloatField()),
                ('total', models.FloatField()),
            ],
        ),
    ]