# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-31 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0052_auto_20171031_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rssfeed',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
