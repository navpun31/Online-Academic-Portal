# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-10 09:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0008_auto_20170910_1356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='description',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='subject_registered',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='website',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='Course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.Course'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='Personal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.Personal'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='Summer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.Summer'),
        ),
    ]