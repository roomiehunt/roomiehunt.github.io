# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0007_auto_20150913_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread_messages',
            name='thread_id',
            field=models.UUIDField(blank=True),
        ),
        migrations.AlterField(
            model_name='threads',
            name='thread_id',
            field=models.UUIDField(blank=True),
        ),
    ]
