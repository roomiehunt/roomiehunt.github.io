# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0010_auto_20151024_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(default=b'FR', max_length=2, choices=[(b'FR', b'Friend_Request'), (b'FA', b'Friend_Accept'), (b'RM', b'Roomate_Request'), (b'RA', b'Roomate_Accept'), (b'NM', b'New_Message'), (b'I', b'Interest shown'), (b'U', b'Unspecified')]),
        ),
    ]
