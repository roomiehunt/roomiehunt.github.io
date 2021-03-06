# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('roomate', '0008_auto_20151026_0102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomate',
            name='id',
        ),
        migrations.AlterField(
            model_name='roomate',
            name='roomate_id',
            field=models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True),
        ),
    ]
