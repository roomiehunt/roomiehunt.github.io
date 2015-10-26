# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0006_auto_20150814_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='private',
            field=models.BooleanField(default=True),
        ),
    ]
