# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roomate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criteria',
            name='cleanliness',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='criteria',
            name='gender',
            field=models.CharField(default=b'U', max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')]),
        ),
    ]
