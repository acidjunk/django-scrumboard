# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('scrumboard', '0007_auto_20150915_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='modified_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 15, 10, 11, 40, 204135)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='modified_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 15, 10, 11, 40, 205204)),
            preserve_default=True,
        ),
    ]
