# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import userprofile.models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0017_auto_20151018_0445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(null=True, upload_to=userprofile.models.upload_location, blank=True),
        ),
    ]
