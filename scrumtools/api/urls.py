from django.conf.urls import url, include
from rest_framework import routers
from scrumtools.api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
#Wishlist
router.register(r'wishes', views.WishViewSet)
#ScrumBoard
router.register(r'statuses', views.StatusViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'sprints', views.SprintViewSet)
router.register(r'stories', views.StoryViewSet)
router.register(r'tasks', views.TaskViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]