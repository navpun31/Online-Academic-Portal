# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-10 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0009_auto_20170910_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='subject_registered',
            field=models.BooleanField(default=False),
        ),
    ]