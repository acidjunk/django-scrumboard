from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from scrumtools.apps.scrumboard import views

urlpatterns = patterns('',
    # ex: /scrumboard/tasklist
    url(r'^$', TemplateView.as_view(template_name='scrumboard/index.html')),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^projectlist/$', views.ProjectList.as_view(), name='project-list'),
    url(r'^projectlist/detail/(?P<pk>\d+)$', views.ProjectDetail.as_view(), name='project-detail'),
    url(r'^projectlist/new$', views.ProjectCreate.as_view(), name='project-new'),
    url(r'^projectlist/edit/(?P<pk>\d+)$', views.ProjectUpdate.as_view(), name='project-edit'),
    url(r'^projectlist/delete/(?P<pk>\d+)$', views.ProjectDelete.as_view(), name='project-delete'),
    url(r'^statuslist/$', views.StatusList.as_view(), name='status-list'),
    url(r'^statuslist/detail/(?P<pk>\d+)$', views.StatusDetail.as_view(), name='status-detail'),
    url(r'^statuslist/new$', views.StatusCreate.as_view(), name='status-new'),
    url(r'^statuslist/edit/(?P<pk>\d+)$', views.StatusUpdate.as_view(), name='status-edit'),
    url(r'^statuslist/delete/(?P<pk>\d+)$', views.StatusDelete.as_view(), name='status-delete'),
    url(r'^sprintlist/$', views.SprintList.as_view(), name='sprint-list'),
    url(r'^sprintlist/detail/(?P<pk>\d+)$', views.SprintDetail.as_view(), name='sprint-detail'),
    url(r'^sprintlist/new$', views.SprintCreate.as_view(), name='sprint-new'),
    url(r'^sprintlist/edit/(?P<pk>\d+)$', views.SprintUpdate.as_view(), name='sprint-edit'),
    url(r'^sprintlist/delete/(?P<pk>\d+)$', views.SprintDelete.as_view(), name='sprint-delete'),
    url(r'^storylist/$', views.StoryList.as_view(), name='story-list'),
    url(r'^storylist/detail/(?P<pk>\d+)$', views.StoryDetail.as_view(), name='story-detail'),
    url(r'^storylist/new$', views.StoryCreate.as_view(), name='story-new'),
    url(r'^storylist/edit/(?P<pk>\d+)$', views.StoryUpdate.as_view(), name='story-edit'),
    url(r'^storylist/delete/(?P<pk>\d+)$', views.StoryDelete.as_view(), name='story-delete'),
    url(r'^tasklist/$', views.TaskList.as_view(), name='task-list'),
    url(r'^tasklist/detail/(?P<pk>\d+)$', views.TaskDetail.as_view(), name='task-detail'),
    url(r'^tasklist/new$', views.TaskCreate.as_view(), name='task-new'),
    url(r'^tasklist/edit/(?P<pk>\d+)$', views.TaskUpdate.as_view(), name='task-edit'),
    url(r'^tasklist/delete/(?P<pk>\d+)$', views.TaskDelete.as_view(), name='task-delete'),
    url(r'^select-project', views.select_project, name='select-project'),
    url(r'^select-sprint', views.select_sprint, name='select-sprint'),
    url(r'^import/$', views.Import.as_view(), name='import'),

)
