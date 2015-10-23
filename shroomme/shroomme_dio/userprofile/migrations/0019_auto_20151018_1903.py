# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import userprofile.models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0018_auto_20151018_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default=b'76de327c-16ed-492b-ae9e-8ff6ca36af65/apple.jpg', upload_to=userprofile.models.upload_location),
        ),
    ]
