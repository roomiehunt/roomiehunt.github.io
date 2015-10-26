# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0003_message_room_rooms'),
    ]

    operations = [
        migrations.AddField(
            model_name='message_room',
            name='user_uuid',
            field=models.UUIDField(null=True, blank=True),
        ),
    ]
