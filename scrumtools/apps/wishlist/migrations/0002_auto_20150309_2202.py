# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wish',
            options={'verbose_name': 'Wish', 'verbose_name_plural': 'Wishes'},
        ),
        migrations.RenameField(
            model_name='wish',
            old_name='content',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='wish',
            old_name='title',
            new_name='name',
        ),
    ]
