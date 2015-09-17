# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('scrumboard', '0006_auto_20150703_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='modified_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 15, 10, 9, 27, 217894)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='modified_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 15, 10, 9, 27, 218858)),
            preserve_default=True,
        ),
    ]
