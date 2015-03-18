from django.contrib.auth.models import User, Group
from scrumtools.apps.wishlist.models import Wish
from scrumtools.apps.scrumboard.models import Project, Sprint, Status, Story, Task
from rest_framework import authentication, permissions, viewsets, filters
from .serializers import UserSerializer, GroupSerializer, WishSerializer, StatusSerializer, ProjectSerializer, SprintSerializer, StorySerializer, TaskSerializer


class DefaultsMixin(object):
    """Default settings for view authentication, permissions, filtering
     and pagination."""

    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    # filter_backends = (
    #     filters.DjangoFilterBackend,
    #     filters.SearchFilter,
    #     filters.OrderingFilter,
    # )

class UserViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

#Wishlist
class WishViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Wish.objects.all()
    serializer_class = WishSerializer

#Scrumboard
class StatusViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class ProjectViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class SprintViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Sprint.objects.order_by('end')
    serializer_class = SprintSerializer
    search_fields = ('name', )
    ordering_fields = ('end', 'name', )

class StoryViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Story.objects.all()
    serializer_class = StorySerializer

class TaskViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer