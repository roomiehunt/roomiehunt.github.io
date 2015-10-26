# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0005_auto_20150821_1237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='id',
        ),
        migrations.AddField(
            model_name='notification',
            name='notification_id',
            field=models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True),
        ),
    ]
