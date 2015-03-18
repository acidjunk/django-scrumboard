from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from scrumtools.apps.scrumboard import views

urlpatterns = patterns('',
    # ex: /scrumboard/tasklist
    url(r'^$', TemplateView.as_view(template_name='scrumboard/index.html')),
    url(r'^projectlist/$', views.ProjectList.as_view(), name='project_list'),
    url(r'^projectlist/detail/(?P<pk>\d+)$', views.ProjectDetail.as_view(), name='project_detail'),
    url(r'^projectlist/new$', views.ProjectCreate.as_view(), name='project_new'),
    url(r'^projectlist/edit/(?P<pk>\d+)$', views.ProjectUpdate.as_view(), name='project_edit'),
    url(r'^projectlist/delete/(?P<pk>\d+)$', views.ProjectDelete.as_view(), name='project_delete'),
    url(r'^statuslist/$', views.StatusList.as_view(), name='status_list'),
    url(r'^statuslist/detail/(?P<pk>\d+)$', views.StatusDetail.as_view(), name='status_detail'),
    url(r'^statuslist/new$', views.StatusCreate.as_view(), name='status_new'),
    url(r'^statuslist/edit/(?P<pk>\d+)$', views.StatusUpdate.as_view(), name='status_edit'),
    url(r'^statuslist/delete/(?P<pk>\d+)$', views.StatusDelete.as_view(), name='status_delete'),
    url(r'^sprintlist/$', views.SprintList.as_view(), name='sprint_list'),
    url(r'^sprintlist/detail/(?P<pk>\d+)$', views.SprintDetail.as_view(), name='sprint_detail'),
    url(r'^sprintlist/new$', views.SprintCreate.as_view(), name='sprint_new'),
    url(r'^sprintlist/edit/(?P<pk>\d+)$', views.SprintUpdate.as_view(), name='sprint_edit'),
    url(r'^sprintlist/delete/(?P<pk>\d+)$', views.SprintDelete.as_view(), name='sprint_delete'),
    url(r'^storylist/$', views.StoryList.as_view(), name='story_list'),
    url(r'^storylist/detail/(?P<pk>\d+)$', views.StoryDetail.as_view(), name='story_detail'),
    url(r'^storylist/new$', views.StoryCreate.as_view(), name='story_new'),
    url(r'^storylist/edit/(?P<pk>\d+)$', views.StoryUpdate.as_view(), name='story_edit'),
    url(r'^storylist/delete/(?P<pk>\d+)$', views.StoryDelete.as_view(), name='story_delete'),
    url(r'^tasklist/$', views.TaskList.as_view(), name='task_list'),
    url(r'^tasklist/detail/(?P<pk>\d+)$', views.TaskDetail.as_view(), name='task_detail'),
    url(r'^tasklist/new$', views.TaskCreate.as_view(), name='task_new'),
    url(r'^tasklist/edit/(?P<pk>\d+)$', views.TaskUpdate.as_view(), name='task_edit'),
    url(r'^tasklist/delete/(?P<pk>\d+)$', views.TaskDelete.as_view(), name='task_delete')
)
