# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-31 08:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0049_rssfeed'),
    ]

    operations = [
        migrations.AddField(
            model_name='rssfeed',
            name='title',
            field=models.CharField(default='', max_length=100, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='rssfeed',
            name='msg',
            field=models.CharField(default='', max_length=300, verbose_name='Message'),
        ),
    ]
