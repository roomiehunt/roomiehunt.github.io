# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('roomate', '0007_roomate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomate',
            name='user1_uuid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='roomate',
            name='user2_uuid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
