# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0004_auto_20150821_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friends',
            name='friends_id',
            field=models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True),
        ),
    ]
