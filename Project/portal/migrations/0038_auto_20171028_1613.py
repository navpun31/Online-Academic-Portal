# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-28 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0037_auto_20171028_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='program',
            field=models.CharField(choices=[('none', 'none'), ('btech', 'btech'), ('mtech', 'mtech'), ('idd', 'idd'), ('phd', 'phd')], default='btech', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='program',
            field=models.CharField(choices=[('none', 'none'), ('btech', 'btech'), ('mtech', 'mtech'), ('idd', 'idd'), ('phd', 'phd')], default='btech', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='program',
            field=models.CharField(choices=[('none', 'none'), ('btech', 'btech'), ('mtech', 'mtech'), ('idd', 'idd'), ('phd', 'phd')], default='none', max_length=100, null=True),
        ),
    ]