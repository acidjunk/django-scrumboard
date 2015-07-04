# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('scrumboard', '0005_auto_20150315_0205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='assigned',
        ),
        migrations.RemoveField(
            model_name='story',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='story',
            name='due',
        ),
        migrations.RemoveField(
            model_name='story',
            name='estimated_days',
        ),
        migrations.RemoveField(
            model_name='story',
            name='started',
        ),
        migrations.RemoveField(
            model_name='story',
            name='status',
        ),
        migrations.RemoveField(
            model_name='story',
            name='story_points',
        ),
        migrations.AlterField(
            model_name='story',
            name='modified_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 3, 22, 46, 4, 188897)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='modified_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 3, 22, 46, 4, 189657)),
            preserve_default=True,
        ),
    ]
