from django.urls import reverse
from django.test import TestCase

from accounts.models import User
from accounts.views.registrations import UserDetailView, UserUpdateView
from accounts.tests.text_mixing import TestMixing


class RegisterViewTest(TestCase):
    def test_get(self):
        response = self.client.get(reverse('accounts:registration'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_post(self):
        response = self.client.post(reverse('accounts:registration'), {
            'username': 'test',
            'email': 'test@email.com',
            'password1': '$password_1234',
            'password2': '$password_1234',
        }, follow=True)
        self.assertRedirects(response, expected_url='/accounts/login/?next=/accounts/detail/',
                             status_code=302, target_status_code=200)
        self.assertEqual(User.objects.count(), 1)


class DetailViewTest(TestMixing, TestCase):
    def test_unauthorized_access(self):
        response = self.client.get(reverse('accounts:detail'))
        self.assertRedirects(response, expected_url='/accounts/login/?next=/accounts/detail/',
                             status_code=302, target_status_code=200)

    def test_authorize_access(self):
        self.client.login(**self.credentials)
        self.client.get(reverse('accounts:login'))

        response = self.client.get(reverse('accounts:detail'))
        self.assertTrue(response.status_code, 200)


    def test_get(self):
        request = self.factory.get('/accounts/detail')
        request.user = self.user

        response = UserDetailView.as_view()(request)
        self.assertEqual(response.status_code, 200)


class UpdateViewTest(TestMixing, TestCase):
    def test_get(self):
        request = self.factory.get('/accounts/update')
        request.user = self.user

        response = UserUpdateView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_post(self):
        self.client.login(**self.credentials)

        response = self.client.post(reverse('accounts:update'), {
            'first_name': 'change',
            'last_name': 'change',
            'email': 'email@email.com'
        })
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'change')
        self.assertEqual(self.user.last_name, 'change')
        self.assertEqual(self.user.email, 'email@email.com')
        self.assertRedirects(response, expected_url=reverse('accounts:detail'), status_code=302, target_status_code=200)
