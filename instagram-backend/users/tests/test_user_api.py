from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

REGISTER_USER_URL = reverse('users:register')
LOGIN_URL = reverse('users:login')
ME_URL = reverse('users:me')

User = get_user_model()


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

    # Dodatek / Zadanie
    # def test_password_too_short(self):
    #     payload = {
    #         'email': 'test@test.com',
    #         'username': 'test',
    #         'password': 'pw'
    #     }
    #     response = self.client.post(REGISTER_USER_URL, payload)

    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #     user_exists = User.objects.filter(
    #         email=payload['email']
    #     ).exists()
    #     self.assertFalse(user_exists)

    # def test_username_too_short(self):
    #     payload = {
    #         'email': 'test@test.com',
    #         'username': 'te',
    #         'password': 'testpass'
    #     }
    #     response = self.client.post(REGISTER_USER_URL, payload)

    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #     user_exists = User.objects.filter(
    #         email=payload['email']
    #     ).exists()
    #     self.assertFalse(user_exists)


class PrivateUserApiTests(TestCase):
    def setUp(self):
        self.user = create_sample_user()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_retrieve_user_unauthorized(self):
        response = APIClient().get(ME_URL)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_user_success(self):
        response = self.client.get(ME_URL)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user_profile(self):
        payload = {
            'username': 'changed',
            'fullname': 'new name',
            'password': 'newpassword123',
        }

        response = self.client.patch(ME_URL, payload)

        self.user.refresh_from_db()
        self.assertEqual(self.user.fullname, payload['fullname'])
        self.assertTrue(self.user.check_password(payload['password']))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
