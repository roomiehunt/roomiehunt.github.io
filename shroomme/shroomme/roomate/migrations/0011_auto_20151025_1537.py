# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roomate', '0010_auto_20151025_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomate',
            name='status',
            field=models.CharField(default=b'U', max_length=1, choices=[(b'R', b'Roomates'), (b'P', b'Pending'), (b'B', b'Blocked'), (b'N', b'Not Roomates')]),
        ),
    ]
