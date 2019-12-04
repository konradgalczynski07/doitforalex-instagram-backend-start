from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

REGISTER_USER_URL = reverse('users:register')
LOGIN_URL = reverse('users:login')

User = get_user_model()


# helper
def create_sample_user(email='test@test.com', username='test', password='testpass'):
    return User.objects.create_user(email, username, password)


class PublicUserApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.payload = {
            'email': 'test@test.com',
            'username': 'test',
            'password': 'testpass',
        }

    def test_register_user_ok(self):
        response = self.client.post(REGISTER_USER_URL, self.payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertNotIn('password', response.data)

    def test_user_exists(self):
        self.client.post(REGISTER_USER_URL, self.payload)
        response = self.client.post(REGISTER_USER_URL, self.payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_ok(self):
        user = create_sample_user()
        payload = {'username': user.username, 'password': 'testpass'}
        response = self.client.post(LOGIN_URL, payload)

        self.assertIn('token', response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_invalid(self):
        payload = {'username': 'test', 'password': 'wrong'}
        response = self.client.post(LOGIN_URL, payload)

        self.assertNotIn('token', response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
