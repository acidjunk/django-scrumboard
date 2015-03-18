# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('votes', models.IntegerField(default=0)),
                ('created_on', models.DateTimeField(verbose_name=b'Creation date')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
