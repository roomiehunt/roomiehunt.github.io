# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roomate', '0002_auto_20151018_0445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criteria',
            name='cleanliness',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'F'), (1, b'E'), (2, b'D'), (3, b'C'), (4, b'B'), (5, b'A')]),
        ),
    ]
