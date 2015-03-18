# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('scrumboard', '0003_auto_20150309_2224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='project',
        ),
        migrations.AlterField(
            model_name='story',
            name='modified_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 10, 22, 40, 15, 138887)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='modified_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 10, 22, 40, 15, 139858)),
            preserve_default=True,
        ),
    ]
