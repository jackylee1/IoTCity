# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-17 16:22
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainserver', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alarm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_min', models.BooleanField(default=True)),
                ('threshold', models.FloatField()),
                ('date_created', models.DateTimeField()),
                ('hours_active_beg', models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(24)])),
                ('hours_active_end', models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(24)])),
            ],
            options={
                'ordering': ('date_created',),
                'verbose_name_plural': 'Alarms',
            },
        ),
        migrations.CreateModel(
            name='AlarmActuator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('alarm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainserver.Alarm')),
            ],
        ),
        migrations.CreateModel(
            name='day_week',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')], max_length=1)),
            ],
            options={
                'verbose_name_plural': 'days_week',
            },
        ),
        migrations.CreateModel(
            name='day_year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'days_year',
            },
        ),
        migrations.CreateModel(
            name='Localization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'Localizations',
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_beginning', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('name', models.TextField(max_length=50)),
                ('information', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('date_beginning',),
                'verbose_name_plural': 'Notes',
            },
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('device_id', models.TextField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=50, unique=True)),
                ('date_added', models.DateTimeField()),
                ('information', models.TextField(null=True)),
                ('address', models.TextField(null=True)),
                ('sensor_type', models.CharField(choices=[('TE', 'Temperature'), ('AI', 'Air'), ('WA', 'Waste'), ('SO', 'Sound'), ('PE', 'People'), ('IL', 'Illumination'), ('RA', 'Radiation')], max_length=2)),
                ('active', models.BooleanField(default=True)),
                ('localization', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainserver.Localization')),
            ],
            options={
                'ordering': ('date_added',),
                'verbose_name_plural': 'Sensors',
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('subscription_id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=50, unique=True)),
                ('date_added', models.DateTimeField()),
                ('working', models.BooleanField(default=True)),
                ('sender', models.BooleanField(default=True)),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainserver.Sensor')),
            ],
            options={
                'ordering': ('date_added',),
                'verbose_name_plural': 'Subscriptions',
            },
        ),
        migrations.CreateModel(
            name='Subscription_Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('information', models.TextField(blank=True, null=True)),
                ('subscriptions', models.ManyToManyField(blank=True, to='mainserver.Subscription')),
                ('users', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('information', models.TextField()),
                ('state', models.CharField(choices=[('NS', 'Not Seen'), ('SE', 'Seen'), ('WI', 'Working on it'), ('SO', 'Solved')], max_length=2)),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainserver.Subscription')),
            ],
            options={
                'ordering': ('date',),
                'verbose_name_plural': 'UserReports',
            },
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.FloatField()),
                ('timeToLive', models.IntegerField(blank=True, default=120, null=True)),
                ('date', models.DateTimeField()),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainserver.Subscription')),
            ],
            options={
                'ordering': ('date',),
                'verbose_name_plural': 'Value',
            },
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='value',
            field=models.FloatField(),
        ),
        migrations.AddField(
            model_name='alarmactuator',
            name='subscription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainserver.Subscription'),
        ),
        migrations.AddField(
            model_name='alarm',
            name='daysOfWeek',
            field=models.ManyToManyField(blank=True, to='mainserver.day_week'),
        ),
        migrations.AddField(
            model_name='alarm',
            name='daysOfYear',
            field=models.ManyToManyField(blank=True, to='mainserver.day_year'),
        ),
        migrations.AddField(
            model_name='alarm',
            name='subscription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainserver.Subscription'),
        ),
        migrations.AddField(
            model_name='alarm',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
