# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-25 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainserver', '0034_sensorsubtype_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensorsubtype',
            name='name',
            field=models.CharField(choices=[('LA', 'Lighting Actuator'), ('C2', 'CO2'), ('VR', 'Visible Radiation'), ('IR', 'Infrared Radiation'), ('WV', 'Waste Volume'), ('WT', 'Waste Internal Temperature'), ('LI', 'Lighting Illumination'), ('PC', 'People Counter'), ('NL', 'Noise Level'), ('UV', 'UV Radiation'), ('AP', 'Air Pressure'), ('WP', 'Waste Fullness Percentage'), ('TE', 'Temperature')], max_length=2, unique=True),
        ),
    ]
