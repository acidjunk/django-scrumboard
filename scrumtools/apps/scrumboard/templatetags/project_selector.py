from django.template import Library
from scrumtools.apps.scrumboard.forms import ProjectForm, SprintForm

register = Library()





def project_selector( value ):
    """
    Shows a dropdown of project and saves them to a session variable
    """
    return range( value )