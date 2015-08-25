# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0008_auto_20150815_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='roomate_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='roomate_status',
            field=models.CharField(default=b'U', max_length=1, choices=[(b'A', b'Looking for roomates '), (b'B', b'Looking for place and roomate'), (b'U', b'Unspecified')]),
        ),
    ]
