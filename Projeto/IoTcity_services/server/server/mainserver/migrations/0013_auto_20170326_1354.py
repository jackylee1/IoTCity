# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-26 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainserver', '0012_auto_20170326_1127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alarm',
            name='subscription',
        ),
        migrations.AddField(
            model_name='alarm',
            name='subscriptions',
            field=models.ManyToManyField(to='mainserver.Subscription'),
        ),
    ]
