# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fields', '0006_auto_20170517_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='xfield',
            name='rule_id',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
