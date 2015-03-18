from __future__ import unicode_literals

import datetime

from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Wish(models.Model):
    #DB fields
    name=models.CharField(max_length=200)
    description=models.TextField()
    votes=models.IntegerField(default=0)
    created_on=models.DateTimeField('Creation date')

    class Meta:
        verbose_name = _('Wish')
        verbose_name_plural = _('Wishes')

    # represent a wish with it's title
    def __str__(self):
        return self.name

    def was_published_recently(self):
        return self.created_on >= timezone.now() - datetime.timedelta(days=1)
    #some extra attributes
    was_published_recently.admin_order_field = 'created_on'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

