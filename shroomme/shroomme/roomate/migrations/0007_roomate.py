# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('roomate', '0006_auto_20151018_2115'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roomate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user1_uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('user2_uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('status', models.CharField(default=b'U', max_length=1, choices=[(b'F', b'Friends'), (b'P', b'Pending'), (b'B', b'Blocked'), (b'N', b'NotFriends')])),
            ],
        ),
    ]
