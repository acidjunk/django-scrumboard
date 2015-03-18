# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('scrumboard', '0002_auto_20150309_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='status',
            field=models.ForeignKey(default=1, to='scrumboard.Status'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='story',
            name='modified_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 9, 22, 24, 50, 965470)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='modified_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 9, 22, 24, 50, 966459)),
            preserve_default=True,
        ),
    ]
