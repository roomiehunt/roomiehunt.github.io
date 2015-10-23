# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roomate', '0003_auto_20151018_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criteria',
            name='cleanliness',
            field=models.IntegerField(default=0, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
        ),
    ]
