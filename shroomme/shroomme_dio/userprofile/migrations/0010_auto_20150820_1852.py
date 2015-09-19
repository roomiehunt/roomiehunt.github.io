# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0009_auto_20150818_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='roomate_status',
            field=models.CharField(default=b'U', max_length=1, choices=[(b'Looking for roomates', b'Looking for roomates'), (b'Looking for place and roomate', b'Looking for place and roomate'), (b'Unspecified', b'Unspecified')]),
        ),
    ]
