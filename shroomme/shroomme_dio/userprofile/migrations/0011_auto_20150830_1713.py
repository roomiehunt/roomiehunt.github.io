# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0010_auto_20150820_1852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='roomate_number',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='roomate_status',
        ),
    ]
