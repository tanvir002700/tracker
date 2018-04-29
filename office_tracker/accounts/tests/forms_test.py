from django.urls import reverse
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser

from accounts.forms import RegistrationForm


class TestMixing(object):
    def setUp(self):
        self.data = {
            'username': 'test',
            'email': 'test@email.com',
            'password1': '$password123',
            'password2': '$password123'
        }


class RegistrationFormTest(TestMixing, TestCase):
    def test_valid_data(self):
        form = RegistrationForm(data=self.data)

        self.assertTrue(form.is_valid())

    def test_with_blank_data(self):
        form = RegistrationForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
                'username': ['This field is required.'],
                'email': ['This field is required.'],
                'password1': ['This field is required.'],
                'password2': ['This field is required.'],
            })
