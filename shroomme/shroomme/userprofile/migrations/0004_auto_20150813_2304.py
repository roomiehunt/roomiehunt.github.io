# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userprofile', '0003_auto_20150810_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user1', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('user2', models.ForeignKey(related_name='friends+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='university',
            field=models.CharField(default=b'Unspecified', max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default=b'Unspecified', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(default=b'U', max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female'), (b'U', b'Unspecified')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default=b'Unspecified', max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='middle_name',
            field=models.CharField(default=b'Unspecified', max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nationality',
            field=models.CharField(default=b'Unspecified', max_length=50, null=True, blank=True),
        ),
    ]
