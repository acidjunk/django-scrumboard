# django-scrumboard
A ScrumBoard app in Django

Warning this app is not ready for production yet. If you want to test it; install alll the requirements in requirements.txt and have a go.
It needs django1.7 and python2 or python3.

Run (from your virtualenv) python manage.py migrate

If you need testdat:

python manage.py createsuperuser
python manage.py loaddata wishlist
python manage.py loaddata scrumboard

Changelog
----------
*v0.1*
-added working DB model
-added CRUD with class based views for wishes, projects, status, stories and tasks
-added some static pages
-addes the starting point for a one page app based on prototype.js, underscore.js and backbone.js
-added a bootstrap3 design
