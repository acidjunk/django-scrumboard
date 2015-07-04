from django.template import Library
from scrumtools.apps.scrumboard.models import Project, Sprint

register = Library()

def project_selector(selected_project=None):
    """
    Shows a current project and link to the selector
    """
    if selected_project:
        project_name=Project.objects.get(pk=selected_project)
    else:
        project_name='No project selected'
    return { 'project_name': project_name}

register.inclusion_tag('tags/project_selector.html')(project_selector)

def sprint_selector(selected_sprint=None):
    """
    Shows a current sprint and link to the selector
    """
    if selected_sprint:
        sprint_name=Sprint.objects.get(pk=selected_sprint)
    else:
        sprint_name='No sprint selected'
    return { 'sprint_name': sprint_name}

register.inclusion_tag('tags/sprint_selector.html')(sprint_selector)
