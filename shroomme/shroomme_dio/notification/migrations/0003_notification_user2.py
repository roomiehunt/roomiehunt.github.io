# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notification', '0002_remove_notification_user2'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='user2',
            field=models.ForeignKey(related_name='notification+', default=1, to=settings.AUTH_USER_MODEL),
        ),
    ]
