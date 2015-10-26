# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('roomate', '0007_roomate'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomate',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='roomate',
            name='roomate_id',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AddField(
            model_name='roomate',
            name='user1',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='roomate',
            name='user2',
            field=models.ForeignKey(related_name='roomate+', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='roomate',
            name='id',
            field=models.IntegerField(default=0, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='roomate',
            name='status',
            field=models.CharField(default=b'U', max_length=1, choices=[(b'R', b'Roomates'), (b'P', b'Pending'), (b'B', b'Blocked'), (b'N', b'Not Roomates')]),
        ),
        migrations.AlterField(
            model_name='roomate',
            name='user1_uuid',
            field=models.UUIDField(default=uuid.uuid4, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='roomate',
            name='user2_uuid',
            field=models.UUIDField(default=uuid.uuid4, null=True, blank=True),
        ),
    ]
