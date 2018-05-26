from django.urls import reverse
from django.test import TestCase

from accounts.tests.text_mixing import TestMixing

class LoginViewTest(TestMixing, TestCase):

    def test_get(self):
        response = self.client.get(reverse('accounts:login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_post(self):
        response = self.client.post(reverse('accounts:login'), **self.credentials, follow=True)
        self.assertEqual(response.status_code, 200)


class LogoutViewTest(TestMixing, TestCase):
    def test_get(self):
        self.client.login(**self.credentials)

        response = self.client.get(reverse('accounts:logout'))
        self.assertRedirects(response, expected_url=reverse('accounts:login'), status_code=302, target_status_code=200)
