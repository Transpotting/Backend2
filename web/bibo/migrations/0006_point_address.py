# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-26 00:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibo', '0005_auto_20160626_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='address',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
