# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0007_profile_private'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friends',
            name='user1',
        ),
        migrations.RemoveField(
            model_name='friends',
            name='user2',
        ),
        migrations.AlterField(
            model_name='profile',
            name='private',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Friends',
        ),
    ]
