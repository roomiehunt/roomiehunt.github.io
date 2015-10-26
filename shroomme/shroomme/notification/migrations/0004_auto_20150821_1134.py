# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0003_notification_user2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='user2',
            field=models.ForeignKey(related_name='notification+', to=settings.AUTH_USER_MODEL),
        ),
    ]
