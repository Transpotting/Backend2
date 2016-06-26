# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bibo', '0004_profile_disabled'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileinvehicle',
            name='lat_in',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profileinvehicle',
            name='lat_out',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profileinvehicle',
            name='lng_in',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profileinvehicle',
            name='lng_out',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='point',
            name='typ',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
