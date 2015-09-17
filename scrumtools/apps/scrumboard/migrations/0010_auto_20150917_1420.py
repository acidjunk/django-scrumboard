# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('scrumboard', '0009_auto_20150917_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='github_project',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='github_id',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='story',
            name='modified_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 17, 14, 20, 41, 820714)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='modified_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 17, 14, 20, 41, 821845)),
            preserve_default=True,
        ),
    ]
