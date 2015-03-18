# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('points', models.IntegerField(default=0)),
                ('estimated', models.IntegerField(default=0)),
                ('created_on', models.DateTimeField(verbose_name=b'Creation date')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('points', models.IntegerField(default=0)),
                ('estimated', models.IntegerField(default=0)),
                ('created_on', models.DateTimeField(verbose_name=b'Creation date')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
