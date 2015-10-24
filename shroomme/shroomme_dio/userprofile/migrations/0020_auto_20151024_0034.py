# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0019_auto_20151018_1903'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='userCriteria',
            new_name='myCriteria',
        ),
    ]
