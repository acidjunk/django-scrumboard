from django import forms

from scrumtools.apps.scrumboard.models import Project, Sprint

# FORM set test stuff
class ProjectForm(forms.Form):
    project_name = forms.ModelChoiceField(Project.objects.all())

class SprintForm(forms.Form):
    sprint_name = forms.ModelChoiceField(Sprint.objects.all())
