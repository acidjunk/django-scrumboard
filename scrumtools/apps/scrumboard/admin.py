from django.contrib import admin

# Register your models here.
from django.contrib import admin
from scrumtools.apps.scrumboard.models import Project, Status, Sprint, Story, Task

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name', 'description']
admin.site.register(Project, ProjectAdmin)

class StatusAdmin(admin.ModelAdmin):
    list_display = ('name','order')
    search_fields = ['name', 'order']
admin.site.register(Status, StatusAdmin)

class SprintAdmin(admin.ModelAdmin):
    list_display = ('project', 'name','description')
    search_fields = ['name', 'description']
admin.site.register(Sprint, SprintAdmin)

class StoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_on', 'was_published_recently')
    list_filter = ['created_on']
    search_fields = ['name', 'description']
admin.site.register(Story, StoryAdmin)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_on', 'was_published_recently')
    list_filter = ['created_on']
    search_fields = ['name', 'description']
admin.site.register(Task, TaskAdmin)