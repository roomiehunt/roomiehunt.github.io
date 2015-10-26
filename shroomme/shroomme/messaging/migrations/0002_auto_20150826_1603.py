# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='user1_uuid',
            field=models.UUIDField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='messages',
            name='user2_uuid',
            field=models.UUIDField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='messages',
            name='user1',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='messages',
            name='user2',
            field=models.ForeignKey(related_name='friends+', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
