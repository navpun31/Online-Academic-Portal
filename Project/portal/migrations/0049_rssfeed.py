# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-31 06:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portal', '0048_auto_20171031_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='rssfeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.CharField(default='', max_length=300)),
                ('date', models.DateTimeField()),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]