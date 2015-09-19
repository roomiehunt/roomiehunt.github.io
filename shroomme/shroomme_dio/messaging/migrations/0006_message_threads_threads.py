# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0005_auto_20150826_1835'),
    ]

    operations = [
        migrations.CreateModel(
            name='message_threads',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('thread_id', models.UUIDField(default=uuid.uuid4, blank=True)),
                ('user_uuid', models.UUIDField(null=True, blank=True)),
                ('message', models.CharField(default=b'Unspecified', max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='threads',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_uuid', models.UUIDField(blank=True)),
                ('thread_id', models.UUIDField(default=uuid.uuid4, blank=True)),
            ],
        ),
    ]
