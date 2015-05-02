from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms.models import modelform_factory

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from scrumtools.apps.scrumboard.models import Project, Status, Sprint, Story, Task

#dashboard
@login_required
def dashboard(request):
    todo_list = [{'title': 'item 1',
                  'content': 'Some bogus content. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla eget ultricies arcu. Vivamus a ex ac neque placerat placerat. Nam vitae suscipit tellus. Duis ut metus sem. Vestibulum molestie, dui sed sodales maximus, lorem dui eleifend nisl, id luctus urna mi at est. Etiam ut lobortis nisl.'},
                 {'title': 'item 2',
                  'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla eget ultricies arcu. Vivamus a ex ac neque placerat placerat. Nam vitae suscipit tellus. Duis ut metus sem.'}]
    progress_list = [{'title': 'item 3',
                      'content': 'Some bogus content. Vestibulum molestie, dui sed sodales maximus, lorem dui eleifend nisl, id luctus urna mi at est. Etiam ut lobortis nisl.'},
                     {'title': 'item 4',
                      'content': 'Some bogus content. Nulla at euismod orci. Mauris suscipit, velit non vestibulum bibendum, lorem massa cursus nisi, posuere consequat massa magna eget enim. Maecenas lobortis elit ex, ac condimentum purus facilisis quis. Sed varius mi ac orci finibus, ac vehicula sem interdum. Nam rhoncus erat non libero vestibulum tincidunt. Curabitur tempor bibendum tellus, eu placerat nibh posuere sed.'}]
    test_list = [{'title': 'item 5',
                  'content': 'Some bogus content. Mauris mattis dolor libero, in porta leo viverra a. Curabitur pharetra nibh mauris. Sed purus urna, fringilla at ornare id, vulputate ut elit. Sed velit ante, facilisis eu finibus nec, efficitur sit amet ex. Proin ac nisl enim. Pellentesque aliquet ligula id sapien efficitur, nec suscipit ipsum faucibus.'},
                 {'title': 'item 6',
                  'content': 'Some bogus content. Sed gravida ornare lacus eu convallis. Nam quis erat sodales, tempor tortor fermentum, fermentum urna. Aliquam porttitor lectus finibus est aliquam mollis.'}]
    done_list = [{'title': 'item 7',
                  'content': 'Some bogus content. Cras non elit bibendum, feugiat metus eu, pellentesque libero. Vivamus at faucibus nulla. Fusce et nunc sit amet felis tristique hendrerit eu sed diam. Ut eget eros laoreet, semper nulla in, bibendum orci.'},
                 {'title': 'item 8', 'content': 'Some bogus content'},
                 {'title': 'item 9', 'content': 'Some bogus content'},
                 {'title': 'item 10', 'content': 'Some bogus content'},
                 {'title': 'item 11', 'content': 'Some bogus content'}]
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