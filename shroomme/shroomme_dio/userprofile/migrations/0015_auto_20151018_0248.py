# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0014_auto_20151018_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='searchCriteria',
            field=models.ForeignKey(related_name='criteria+', blank=True, to='roomate.Criteria', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='userCriteria',
            field=models.ForeignKey(blank=True, to='roomate.Criteria', null=True),
        ),
    ]
