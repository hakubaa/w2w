# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-08 20:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20160908_1931'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preflist',
            old_name='pref',
            new_name='movies',
        ),
        migrations.AlterField(
            model_name='moviepref',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pref', to='tmdb.Movie'),
        ),
        migrations.AlterField(
            model_name='moviepref',
            name='preflist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data', to='accounts.PrefList'),
        ),
    ]
