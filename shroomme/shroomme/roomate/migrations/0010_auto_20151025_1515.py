# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('roomate', '0009_auto_20151025_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomate',
            name='user2',
            field=models.ForeignKey(related_name='roomate+', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
