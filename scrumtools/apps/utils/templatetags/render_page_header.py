from django import template

register = template.Library()

#renders page title with new button and searchform
def render_page_header_complete(title, icon, new_object_name, new_object_url, quicksearch):
    return {'title': title, 'icon': icon, 'new_object_name': new_object_name, 'new_object_url': new_object_url, 'quicksearch': quicksearch}

#renders page title with new button
def render_page_header_normal(title, icon, new_object_name, new_object_url):
    return {'title': title, 'icon': icon, 'new_object_name': new_object_name, 'new_object_url': new_object_url}

#renders page title
def render_page_header_simple(title, icon):
    return {'title': title, 'icon': icon }

register.inclusion_tag('page_header_complete.html')(render_page_header_complete)
register.inclusion_tag('page_header_normal.html')(render_page_header_normal)
register.inclusion_tag('page_header_simple.html')(render_page_header_simple)