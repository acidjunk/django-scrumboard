# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scrumboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default='', max_length=200, blank=True)),
                ('description', models.TextField(default='', blank=True)),
                ('developer_days', models.SmallIntegerField()),
                ('end', models.DateField()),
                ('project', models.ForeignKey(to='scrumboard.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('order', models.IntegerField()),
                ('project', models.ForeignKey(to='scrumboard.Project')),
            ],
            options={
                'ordering': ('order',),
                'verbose_name': 'Status',
                'verbose_name_plural': 'Statuses',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='story',
            options={'verbose_name': 'Story', 'verbose_name_plural': 'Stories'},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Task', 'verbose_name_plural': 'Tasks'},
        ),
        migrations.RenameField(
            model_name='story',
            old_name='content',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='story',
            old_name='estimated',
            new_name='estimated_days',
        ),
        migrations.RenameField(
            model_name='story',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='story',
            old_name='points',
            new_name='story_points',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='content',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='estimated',
            new_name='estimated_days',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='points',
            new_name='story_points',
        ),
        migrations.AddField(
            model_name='story',
            name='assigned',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='story',
            name='completed',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='story',
            name='due',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='story',
            name='modified_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 9, 22, 1, 41, 114384)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='story',
            name='project',
            field=models.ForeignKey(default=1, to='scrumboard.Project'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='story',
            name='sprint',
            field=models.ForeignKey(blank=True, to='scrumboard.Sprint', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='story',
            name='started',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='assigned',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='completed',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='due',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='modified_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 9, 22, 1, 41, 115335)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default=1, to='scrumboard.Project'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='sprint',
            field=models.ForeignKey(blank=True, to='scrumboard.Sprint', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='started',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.ForeignKey(default=1, to='scrumboard.Status'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='story',
            field=models.ForeignKey(blank=True, to='scrumboard.Story', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='story',
            name='created_on',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='created_on',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
