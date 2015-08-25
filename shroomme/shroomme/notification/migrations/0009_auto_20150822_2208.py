# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0008_auto_20150821_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='user1_uuid',
            field=models.UUIDField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='user2_uuid',
            field=models.UUIDField(null=True, blank=True),
        ),
    ]
