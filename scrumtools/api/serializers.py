from datetime import date

from django.contrib.auth.models import User, Group
from scrumtools.apps.wishlist.models import Wish
from scrumtools.apps.scrumboard.models import Status, Project, Sprint, Story, Task
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

#Wishlist
class WishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Wish
        fields = ('url', 'name', 'description', 'created_on', 'votes')

#ScrumBoard
class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status
        fields = ('url', 'name')

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('url', 'name')

class SprintSerializer(serializers.ModelSerializer):

    #links = serializers.SerializerMethodField()

    class Meta:
        model = Sprint
        fields = ('id', 'project', 'name', 'description', 'developer_days', 'end')

    # def get_links(self, obj):
    #     request = self.context['request']
    #     return {
    #         'self': reverse('sprint-detail',
    #             kwargs={'pk': obj.pk},request=request),
    #         'tasks': reverse('task-list',
    #         	request=request) + '?sprint={}'.format(obj.pk),
    #     }

    def validate_end(self, value):
        new = self.instance is None
        changed = self.instance and self.instance.end != value
        if (new or changed) and (value < date.today()):
            msg = _('End date cannot be in the past.')
            raise serializers.ValidationError(msg)
        return value

class StorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Story
        fields = ('url', 'name')

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('url', 'name')