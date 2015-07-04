from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from .models import Project, Sprint, Story, Task, Status

# Create your tests here.
class ScrumboardTestCase(TestCase):
    def setUp(self):
        project = Project.objects.create(name="testproject")
        Sprint.objects.create(name="sprint 1", developer_days=10, project=project, end=timezone.now() + timedelta(days=7))
        Sprint.objects.create(name="sprint 2", developer_days=20, project=project, end=timezone.now() + timedelta(days=14))


    def test_sprint_has_date_in_future(self):
        """Test if setting a sprint date went ok"""
        sprint1 = Sprint.objects.get(pk=1)
        self.assertGreater(sprint1.end, timezone.now().date())
        sprint2 = Sprint.objects.get(pk=2)
        self.assertGreater(sprint2.end, timezone.now().date())
