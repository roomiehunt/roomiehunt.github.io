# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0003_auto_20150821_2235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friends',
            old_name='relation_id',
            new_name='friends_id',
        ),
    ]
