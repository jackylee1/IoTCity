# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-28 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainserver', '0039_auto_20170428_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='sensor_type',
            field=models.CharField(choices=[('TE', 'Temperature'), ('AI', 'Air'), ('WA', 'Waste'), ('SO', 'Noise'), ('PE', 'People'), ('IL', 'Lighting'), ('RA', 'Radiation'), ('LO', 'Localization')], max_length=2),
        ),
        migrations.AlterField(
            model_name='sensorsubtype',
            name='name',
            field=models.CharField(choices=[('LA', 'Lighting Actuator'), ('C2', 'CO2'), ('VR', 'Visible Radiation'), ('IR', 'Infrared Radiation'), ('WV', 'Waste Volume'), ('WT', 'Waste Internal Temperature'), ('LI', 'Lighting Illumination'), ('PC', 'People Counter'), ('NL', 'Noise Level'), ('UV', 'UV Radiation'), ('AP', 'Air Pressure'), ('WP', 'Waste Fullness Percentage'), ('TE', 'Temperature'), ('LA', 'Latitude'), ('LO', 'Longitude')], max_length=2, unique=True),
        ),
    ]
