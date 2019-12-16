# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-28 09:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0029_auto_20171028_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='year',
            field=models.CharField(choices=[('First', 'I'), ('Second', 'II'), ('Third', 'III'), ('Fourth', 'IV'), ('Fifth', 'V')], default='First', max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='batch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Batch'),
        ),
    ]