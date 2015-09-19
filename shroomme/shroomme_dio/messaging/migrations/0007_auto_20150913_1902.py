# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0006_message_threads_threads'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='message_threads',
            new_name='thread_messages',
        ),
    ]
