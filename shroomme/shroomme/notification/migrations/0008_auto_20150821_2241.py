# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0007_notification_target_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='target_id',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
