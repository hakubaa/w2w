# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-08 21:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20160908_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_real',
            field=models.BooleanField(default=True),
        ),
    ]
