from rest_framework.test import APITestCase
from rest_framework import status
from ...models import User
from rest_framework.reverse import reverse


class UserViewTests(APITestCase):
    def setUp(self):
        self.user = User(email='test@test.com', password='abc@123456')
        self.user.save()

    def test_register_user_and_return_user_token(self):
        data = {'email': 'test1@gmail.com', 'password': 'abd@123455'}
        response = self.client.post(reverse('user_view'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(response.data['access_token'])

    def test_login_user_and_return_user_token(self):
        data = {'email': 'test@test.com', 'password': 'abc@123456'}
        response = self.client.post(reverse('user_view'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data['access_token'])

    def test_update_password_and_return_user_token(self):
        data = {'email': 'test@test.com', 'previous_password': 'abc@123456', 'password': 'abc@1234567'}
        response = self.client.put(reverse('user_view'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data['access_token'])
