from django.test import RequestFactory
from accounts.models import User

class TestMixing(object):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='jacob', email='jacob@test.com', password='top_secret')
        self.credentials = {
            'username': 'jacob',
            'password': 'top_secret'
        }
