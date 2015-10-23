# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roomate', '0001_initial'),
        ('userprofile', '0013_auto_20151017_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='searchCriteria',
            field=models.ForeignKey(related_name='searchCriteria', blank=True, to='roomate.Criteria', null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='userCriteria',
            field=models.ForeignKey(related_name='userCriteria', blank=True, to='roomate.Criteria', null=True),
        ),
    ]
