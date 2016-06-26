# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bibo', '0003_auto_20160625_2352'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='disabled',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
