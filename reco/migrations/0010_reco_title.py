# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-15 10:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reco', '0009_auto_20161015_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='reco',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
    ]
