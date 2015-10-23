# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roomate', '0005_auto_20151018_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criteria',
            name='budget',
            field=models.IntegerField(default=0),
        ),
    ]
