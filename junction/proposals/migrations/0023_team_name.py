# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-01 07:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0022_auto_20170601_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='name',
            field=models.CharField(default='Temp team name', max_length=255),
            preserve_default=False,
        ),
    ]