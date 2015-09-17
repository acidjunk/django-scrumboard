# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('scrumboard', '0008_auto_20150915_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='modified_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 17, 12, 3, 22, 466422)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='modified_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 17, 12, 3, 22, 467348)),
            preserve_default=True,
        ),
    ]
