# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0002_auto_20150820_1956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friends',
            name='id',
        ),
        migrations.AddField(
            model_name='friends',
            name='relation_id',
            field=models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True),
        ),
    ]
