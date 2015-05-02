from django import template

register = template.Library()

def show_search(quicksearch):
    return {'quicksearch': quicksearch}

register.inclusion_tag('show_search.html')(show_search)