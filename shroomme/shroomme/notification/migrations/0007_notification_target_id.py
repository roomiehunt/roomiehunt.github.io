# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0006_auto_20150821_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='target_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
