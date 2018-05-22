from django.urls import reverse
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser
from datetime import datetime

from leave_tracker.models import Leave


class TestMixing(object):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='jacob',
                                             email='jacob@test.com',
                                             password='top_secret')
        self.credentials = {
            'username': 'jacob',
            'password': 'top_secret'
        }


class TestLeaveListView(TestCase):
    pass


class TestLeaveDetailView(TestCase):
    pass


class TestLeaveCreateView(TestCase):
    pass


class TestLeaveUpdateView(TestCase):
    pass


class TestLeaveDeleteView(TestCase):
    pass
