from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms.models import modelform_factory

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from scrumtools.apps.scrumboard.models import Project, Status, Sprint, Story, Task
from scrumtools.apps.scrumboard.forms import ProjectForm, SprintForm

import json
import urllib2
data = json.load(urllib2.urlopen("https://api.github.com/repos/acidjunk/django-scrumboard/issues"))


#dashboard
@login_required
def dashboard(request):
    todo_list = []
    progress_list = []
    test_list = []
    done_list = []

    for i in data:
        todo_list.append({'title': i['number'], 'content': i['title']})
        progress_list.append({'title': i['number'], 'content': i['title']})
        test_list.append({'title': i['number'], 'content': i['title']})
        done_list.append({'title': i['number'], 'content': i['title']})

    context_dict = {
        'todo_list': todo_list,
        'progress_list': progress_list,
        'test_list': test_list,
        'done_list': done_list,
    }
    return render(request, 'scrumboard/dashboard.html', context_dict)

#Projects
class ProjectList(ListView):
    model = Project
    paginate_by = 10

class ProjectCreate(CreateView):
    model = Project
    success_url = reverse_lazy('scrumboard:project-list')
    template_name = 'scrumboard/form.html'

class ProjectUpdate(UpdateView):
    model = Project
    success_url = reverse_lazy('scrumboard:project-list')
    template_name = 'scrumboard/form.html'

class ProjectDelete(DeleteView):
    model = Project
    success_url = reverse_lazy('scrumboard:project-list')
    template_name = 'scrumboard/confirm_delete.html'

class ProjectDetail(DetailView):
    model = Project

#Statusses
class StatusList(ListView):
    model = Status
    paginate_by = 10

class StatusCreate(CreateView):
    model = Status
    success_url = reverse_lazy('scrumboard:status-list')
    template_name = 'scrumboard/form.html'

class StatusUpdate(UpdateView):
    model = Status
    success_url = reverse_lazy('scrumboard:status-list')
    template_name = 'scrumboard/form.html'

class StatusDelete(DeleteView):
    model = Status
    success_url = reverse_lazy('scrumboard:status-list')
    template_name = 'scrumboard/confirm_delete.html'


class StatusDetail(DetailView):
    model = Status

#Sprints
class SprintList(ListView):
    model = Sprint
    paginate_by = 10

class SprintCreate(CreateView):
    model = Sprint
    success_url = reverse_lazy('scrumboard:sprint-list')
    template_name = 'scrumboard/form.html'

class SprintUpdate(UpdateView):
    model = Sprint
    success_url = reverse_lazy('scrumboard:sprint-list')
    template_name = 'scrumboard/form.html'

class SprintDelete(DeleteView):
    model = Sprint
    success_url = reverse_lazy('scrumboard:sprint-list')
    template_name = 'scrumboard/confirm_delete.html'

class SprintDetail(DetailView):
    model = Sprint

#Stories
class StoryList(ListView):
    model = Story
    paginate_by = 10

class StoryCreate(CreateView):
    model = Story
    form_class = modelform_factory(Story)
    success_url = reverse_lazy('scrumboard:story-list')
    template_name = 'scrumboard/form.html'

class StoryUpdate(UpdateView):
    model = Story
    form_class = modelform_factory(Story)
    success_url = reverse_lazy('scrumboard:story-list')
    template_name = 'scrumboard/form.html'

class StoryDelete(DeleteView):
    model = Story
    success_url = reverse_lazy('scrumboard:story-list')
    template_name = 'scrumboard/confirm_delete.html'

class StoryDetail(DetailView):
    model = Story

#Tasks
class TaskList(ListView):
    model = Task
    paginate_by = 10

class TaskCreate(CreateView):
    model = Task
    form_class = modelform_factory(Task)
    success_url = reverse_lazy('scrumboard:task-list')
    template_name = 'scrumboard/form.html'

class TaskUpdate(UpdateView):
    model = Task
    form_class = modelform_factory(Task)
    success_url = reverse_lazy('scrumboard:task-list')
    template_name = 'scrumboard/form.html'

class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('scrumboard:task-list')
    template_name = 'scrumboard/confirm_delete.html'

class TaskDetail(DetailView):
    model = Task

class GetIssues(TemplateView): # import
    for i in data:
        task = Task()
        task.Project = "Project 1"
        task.name = i['number']
        task.description = i['title']
        task.Status = "Stat1"
        task.Sprint = "Meer koffie"
        task.Story = ""
        task.Story_points = 1
        task.estimated_days = 5
        task.created_on = "2015-01-01"  # date(2015,1,1)
        task.modified_on = "2015-05-03"  # date(2015,5,3)
        # task.assigned
        task.started = "2015-01-01"
        task.due = "2015-05-03"
        task.completed = "2015-08-08"
        task.save()


def select_project(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProjectForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            request.session['selected_project']=request.POST.get('project_name', None)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProjectForm(initial={'project_name': request.session['selected_project']})
    context_dict = {
        'form':form
    }
    return render(request, 'scrumboard/select_project.html', context_dict)


def select_sprint(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SprintForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            request.session['selected_sprint']=request.POST.get('sprint_name', None)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SprintForm(initial={'sprint_name': request.session['selected_sprint']})
    context_dict = {
        'form':form
    }
    return render(request, 'scrumboard/select_sprint.html', context_dict)