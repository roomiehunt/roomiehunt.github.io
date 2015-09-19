# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0006_auto_20150822_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friends',
            name='status',
            field=models.CharField(default=b'U', max_length=1, choices=[(b'F', b'Friends'), (b'P', b'Pending'), (b'B', b'Blocked'), (b'N', b'NotFriends')]),
        ),
    ]
