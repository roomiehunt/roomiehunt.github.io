# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0002_auto_20150826_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='message_room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('room_uuid', models.UUIDField(default=uuid.uuid4, blank=True)),
                ('message', models.CharField(default=b'Unspecified', max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='rooms',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_uuid', models.UUIDField(blank=True)),
                ('room_uuid', models.UUIDField(default=uuid.uuid4, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
