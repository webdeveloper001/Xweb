# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fields', '0010_auto_20170517_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xfield',
            name='rule',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
