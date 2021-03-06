# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-28 09:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0031_auto_20171028_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='Batch',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='portal.Batch'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='batch',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='portal.Batch'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='batch',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='portal.Batch'),
        ),
    ]
