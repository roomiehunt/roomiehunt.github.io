# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0004_auto_20150821_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(default=b'FR', max_length=2, choices=[(b'FR', b'Friend_Request'), (b'FA', b'Friend_Accept'), (b'NM', b'New_Message'), (b'U', b'Unspecified')]),
        ),
    ]
