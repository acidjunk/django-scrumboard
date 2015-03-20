from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms.models import modelform_factory
from datetimewidget.widgets import DateTimeWidget

from django.core.urlresolvers import reverse_lazy

from scrumtools.apps.scrumboard.models import Project, Status, Sprint, Story, Task

#Projects
class ProjectList(ListView):
    model = Project
    paginate_by = 10

class ProjectCreate(CreateView):
    model = Project
    success_url = reverse_lazy('scrumboard:project_list')

class ProjectUpdate(UpdateView):
    model = Project
    success_url = reverse_lazy('scrumboard:project_list')

class ProjectDelete(DeleteView):
    model = Project
    success_url = reverse_lazy('scrumboard:project_list')

class ProjectDetail(DetailView):
    model = Project

#Statusses
class StatusList(ListView):
    model = Status
    paginate_by = 10

class StatusCreate(CreateView):
    model = Status
    success_url = reverse_lazy('scrumboard:status_list')

class StatusUpdate(UpdateView):
    model = Status
    success_url = reverse_lazy('scrumboard:status_list')

class StatusDelete(DeleteView):
    model = Status
    success_url = reverse_lazy('scrumboard:status_list')

class StatusDetail(DetailView):
    model = Status

#Sprints
class SprintList(ListView):
    model = Sprint
    paginate_by = 10

class SprintCreate(CreateView):
    model = Sprint
    success_url = reverse_lazy('scrumboard:sprint_list')

class SprintUpdate(UpdateView):
    model = Sprint
    success_url = reverse_lazy('scrumboard:sprint_list')

class SprintDelete(DeleteView):
    model = Sprint
    success_url = reverse_lazy('scrumboard:sprint_list')

class SprintDetail(DetailView):
    model = Sprint

#Stories
class StoryList(ListView):
    model = Story
    paginate_by = 10

class StoryCreate(CreateView):
    model = Story
    form_class = modelform_factory(Story, widgets={"created_on": DateTimeWidget(usel10n=True, bootstrap_version=3)})
    success_url = reverse_lazy('scrumboard:story_list')

class StoryUpdate(UpdateView):
    model = Story
    form_class = modelform_factory(Story, widgets={"created_on": DateTimeWidget(usel10n=True, bootstrap_version=3)})
    success_url = reverse_lazy('scrumboard:story_list')

class StoryDelete(DeleteView):
    model = Story
    success_url = reverse_lazy('scrumboard:story_list')

class StoryDetail(DetailView):
    model = Story

#Tasks
class TaskList(ListView):
    model = Task
    paginate_by = 10

class TaskCreate(CreateView):
    model = Task
    form_class = modelform_factory(Task, widgets={"created_on": DateTimeWidget(usel10n=True, bootstrap_version=3),"modified_on": DateTimeWidget(usel10n=True, bootstrap_version=3)})
    success_url = reverse_lazy('scrumboard:task_list')

class TaskUpdate(UpdateView):
    model = Task
    form_class = modelform_factory(Task, widgets={"created_on": DateTimeWidget(usel10n=True, bootstrap_version=3),"modified_on": DateTimeWidget(usel10n=True, bootstrap_version=3)})
    success_url = reverse_lazy('scrumboard:task_list')

class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('scrumboard:task_list')

class TaskDetail(DetailView):
    model = Task