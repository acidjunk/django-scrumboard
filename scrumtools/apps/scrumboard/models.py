# Models for a ScrumBoard
# TODO: come up with a clever way to have one work unit that can be a Story or a Task

from __future__ import unicode_literals

import datetime

from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Project(models.Model):
    name = models.CharField(max_length=100)
    github_project = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Sprint(models.Model):
    """Development iteration period."""
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=200, blank=True, default='')
    description = models.TextField(blank=True, default='')
    developer_days = models.SmallIntegerField()
    end = models.DateField()

    def __str__(self):
        return self.name or _('Sprint ending %s') % self.end

@python_2_unicode_compatible
class Status(models.Model):
    name = models.CharField(max_length=64) # e.g. Todo, In progress, Testing Done
    order = models.IntegerField()

    class Meta:
        verbose_name = _('Status')
        verbose_name_plural = _('Statuses')
        ordering = ('order',)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Story(models.Model):
    """Unit of work to be done for the sprint. Can consist out of smaller tasks"""
    project = models.ForeignKey(Project)
    name=models.CharField(max_length=200)
    description=models.TextField()
    sprint = models.ForeignKey(Sprint, blank=True, null=True)
    created_on=models.DateTimeField()
    modified_on=models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = _('Story')
        verbose_name_plural = _('Stories')

    # represent a story with it's title
    def __str__(self):
        return self.name

    def was_published_recently(self):
        return self.created_on >= timezone.now() - datetime.timedelta(days=1)
    #some extra attributes
    was_published_recently.admin_order_field = 'created_on'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

@python_2_unicode_compatible
class Task(models.Model):
    """Smallest unit of work to be done for the sprint."""
    project = models.ForeignKey(Project)
    name=models.CharField(max_length=200)
    github_id = models.IntegerField(default=0)
    description=models.TextField()
    status = models.ForeignKey(Status)
    sprint = models.ForeignKey(Sprint, blank=True, null=True)
    story = models.ForeignKey(Story, blank=True, null=True)
    story_points=models.IntegerField(default=0)
    estimated_days=models.IntegerField(default=0)
    created_on=models.DateTimeField()
    modified_on=models.DateTimeField(default=timezone.now)
    assigned = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    started = models.DateField(blank=True, null=True)
    due = models.DateField(blank=True, null=True)
    completed = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')

    # represent a task with it's title
    def __str__(self):
        return self.name

    def was_published_recently(self):
        return self.created_on >= timezone.now() - datetime.timedelta(days=1)
    #some extra attributes
    was_published_recently.admin_order_field = 'created_on'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
