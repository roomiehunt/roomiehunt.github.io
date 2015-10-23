# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Criteria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('major', models.CharField(default=b'Unspecified', max_length=50, null=True, blank=True)),
                ('hobby', models.CharField(default=b'Unspecified', max_length=50, null=True, blank=True)),
                ('smoke', models.CharField(default=b'Unspecified', max_length=50, null=True, blank=True)),
                ('pet', models.CharField(default=b'Unspecified', max_length=50, null=True, blank=True)),
                ('relationship_status', models.CharField(default=b'Unspecified', max_length=50, null=True, blank=True)),
                ('gender', models.CharField(default=b'U', max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female'), (b'U', b'Unspecified')])),
                ('nationality', models.CharField(default=b'Unspecified', max_length=50, null=True, blank=True)),
                ('cleanliness', models.CharField(default=b'Unspecified', max_length=50, null=True, blank=True)),
                ('sleeping_habit', models.CharField(default=b'Unspecified', max_length=50, null=True, blank=True)),
                ('drinking', models.CharField(default=b'Unspecified', max_length=50, null=True, blank=True)),
                ('noisiness', models.CharField(default=b'Unspecified', max_length=50, null=True, blank=True)),
                ('overnight_guests', models.CharField(default=b'Unspecified', max_length=50, null=True, blank=True)),
                ('cooking', models.CharField(default=b'Unspecified', max_length=50, null=True, blank=True)),
                ('budget', models.CharField(default=b'Unspecified', max_length=50, null=True, blank=True)),
            ],
        ),
    ]
