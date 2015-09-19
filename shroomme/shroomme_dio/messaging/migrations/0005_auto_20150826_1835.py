# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0004_message_room_user_uuid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messages',
            old_name='created',
            new_name='timestamp',
        ),
    ]
