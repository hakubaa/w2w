# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-07 21:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reco', '0002_auto_20160907_2146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reco',
            old_name='movies',
            new_name='base',
        ),
    ]