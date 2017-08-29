# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-29 10:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0014_conferencesettings'),
        ('proposals', '0024_auto_20170829_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='conference',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='conferences.Conference'),
        ),
    ]