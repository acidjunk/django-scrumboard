from sitetree.utils import tree, item

'''
RUN:
delete site tree from admin menu and run:
python manage.py sitetree_resync_apps
or to regenerate the menu in 1 command run
scripts/regenerate_menu.sh
'''

# Be sure you defined `sitetrees` in your module. The treem item hint value is used to show icons when possible.
sitetrees = (
    # Define a tree with `tree` function.
    tree('main_en', items=[
        # Then define items and their children with `item` function.
        item('Home', '/', access_loggedin=False, access_guest=True, url_as_pattern=False, hint='home'),
        item('Home', '/scrumboard/dashboard', access_loggedin=True, access_guest=False, url_as_pattern=False, hint='home'), # set alternative home for logged in users
        item('Wishlist', '', access_loggedin=True, url_as_pattern=False, hint='shop', children=[
            item('List Wishes', 'wishlist:wish-list', access_loggedin=True, in_menu=True, in_sitetree=True, hint='list'),
            item('Add Wishes', 'wishlist:wish-new', access_loggedin=True, in_menu=True, in_sitetree=True, hint='plus'),
            item('Edit Wish"{{ wish.name }}"', 'wishlist:wish-edit wish.id', access_loggedin=True, in_menu=False, in_sitetree=False, hint='edit'),
            item('View Wish "{{ wish.name }}', 'wishlist:wish-detail wish.id', access_loggedin=True, in_menu=False, in_sitetree=False, hint='search'),
            item('Delete Wish "{{ wish.name }}"', 'wishlist:wish-delete wish.id', access_loggedin=True, in_menu=False, in_sitetree=False, hint='trash'),
        ]),
        item('Scrumboard', '', access_loggedin=True, url_as_pattern=False, hint='windows', children=[
            item('Dashboard', '/scrumboard/dashboard', access_loggedin=True, access_guest=False, url_as_pattern=False, hint='windows'), # set alternative home for logged in users
            item('List Sprints', 'scrumboard:sprint-list',  access_loggedin=True, in_menu=True, in_sitetree=True, hint='list'),
            item('Add Sprint', 'scrumboard:sprint-new',access_loggedin=True, in_menu=True, in_sitetree=True, hint='plus'),
            item('Edit Sprint "{{ sprint.name }}"', 'scrumboard:sprint-edit sprint.id', access_loggedin=True, in_menu=False, in_sitetree=False, hint='edit'),
            item('View Sprint "{{ sprint.name }}"', 'scrumboard:sprint-detail sprint.id', access_loggedin=True, in_menu=False, in_sitetree=False, hint='search'),
            item('Delete Sprint "{{ sprint.name }}"', 'scrumboard:sprint-delete sprint.id', access_loggedin=True, in_menu=False, in_sitetree=False, hint='trash'),
            item('List Stories', 'scrumboard:story-list', access_loggedin=True, in_menu=True, in_sitetree=True, hint='list'),
            item('Add Story', 'scrumboard:story-new', access_loggedin=True, in_menu=True, in_sitetree=True, hint='plus'),
            item('Edit Story "{{ story.name }}"', 'scrumboard:story-edit story.id', access_loggedin=True, in_menu=False, in_sitetree=False, hint='edit'),
            item('View Story "{{ story.name }}"', 'scrumboard:story-detail story.id', access_loggedin=True, in_menu=False, in_sitetree=False, hint='search'),
            item('Delete Story "{{ story.name }}"', 'scrumboard:story-delete story.id', access_loggedin=True, in_menu=False, in_sitetree=False, hint='trash'),
            item('List Task', 'scrumboard:task-list', access_loggedin=True, in_menu=True, in_sitetree=True, hint='list'),
            item('Add Task', 'scrumboard:task-new', access_loggedin=True, in_menu=True, in_sitetree=True, hint='plus'),
            item('Edit Task "{{ task.name }}"', 'scrumboard:task-edit task.id', access_loggedin=True, in_menu=False, in_sitetree=False, hint='edit'),
            item('View Task "{{ task.name }}"', 'scrumboard:task-detail task.id', access_loggedin=True, in_menu=False, in_sitetree=False, hint='search'),
            item('Delete Task "{{ task.name }}"', 'scrumboard:task-delete task.id', access_loggedin=True, in_menu=False, in_sitetree=False, hint='trash'),
        ]),
        item('Project', '', access_loggedin=True, url_as_pattern=False, hint='settings', children=[
            item('List Projects', 'scrumboard:project-list', access_loggedin=True, in_menu=True, in_sitetree=True, hint='list'),
            item('Add Project', 'scrumboard:project-new', access_loggedin=True, in_menu=True, in_sitetree=True, hint='plus'),
            item('Edit "{{ project.name }}"', 'scrumboard:project-edit project.id', access_loggedin=True, in_menu=False, in_sitetree=False, hint='edit'),
            item('View Sprint "{{ project.name }}"', 'scrumboard:project-detail project.id', access_loggedin=True, in_menu=False, in_sitetree=False, hint='search'),
            item('Delete Sprint "{{ project.name }}"', 'scrumboard:project-delete project.id', access_loggedin=True, in_menu=False, in_sitetree=False, hint='trash'),
            item('List Statuses', 'scrumboard:status-list', access_loggedin=True, in_menu=True, in_sitetree=True, hint='list'),
            item('Add Status', 'scrumboard:status-new', access_loggedin=True, in_menu=True, in_sitetree=True, hint='plus'),
            item('Edit Status "{{ status.name }}"', 'scrumboard:status-edit status.id', access_loggedin=True, in_menu=False, in_sitetree=False, hint='edit'),
            item('View Status "{{ status.name }}"', 'scrumboard:status-detail status.id', access_loggedin=True, in_menu=False, in_sitetree=False, hint='search'),
            item('Delete Status "{{ status.name }}"', 'scrumboard:status-delete status.id', access_loggedin=True, in_menu=False, in_sitetree=False, hint='trash'),
        ]),
        item('Help', '/page/help/', url_as_pattern=False, hint='question', children=[
            item('Wishlist help', '/page/help-wishlist', url_as_pattern=False, in_menu=True, in_sitetree=True, hint='shop'),
            item('Scrumboard help', '/page/help-scrumboard', url_as_pattern=False, in_menu=True, in_sitetree=True, hint='windows'),
        ]),
        #item('Logout', '/logout?next=/', access_loggedin=True, url_as_pattern=False, hint='sign out'),
        item('Login', '/login?next=/', access_guest=True, url_as_pattern=False, hint='sign in'),
    ]),
)