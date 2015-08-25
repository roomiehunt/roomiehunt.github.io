# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0005_auto_20150821_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='friends',
            name='user1_uuid',
            field=models.UUIDField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='friends',
            name='user2_uuid',
            field=models.UUIDField(null=True, blank=True),
        ),
    ]
