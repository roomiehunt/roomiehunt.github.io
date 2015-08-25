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
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(default=b'Unspecified', max_length=50)),
                ('read', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('notification_type', models.CharField(default=b'F', max_length=1, choices=[(b'F', b'Friend_Request'), (b'M', b'New_Message'), (b'U', b'Unspecified')])),
                ('user1', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('user2', models.ForeignKey(related_name='notification+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
