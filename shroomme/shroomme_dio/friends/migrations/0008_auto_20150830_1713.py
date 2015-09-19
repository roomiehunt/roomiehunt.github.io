# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0007_auto_20150826_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='friends',
            name='user1_last_received',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 30, 22, 13, 48, 441000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='friends',
            name='user1_messages_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='friends',
            name='user2_last_received',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 30, 22, 13, 52, 679000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='friends',
            name='user2_messages_count',
            field=models.IntegerField(default=0),
        ),
    ]
