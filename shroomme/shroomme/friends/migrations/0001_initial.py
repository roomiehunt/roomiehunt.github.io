# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=b'U', max_length=1, choices=[(b'U', b'Unfriends'), (b'F', b'Friends'), (b'P', b'Pending'), (b'B', b'Blocked')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user1', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('user2', models.ForeignKey(related_name='friends+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
