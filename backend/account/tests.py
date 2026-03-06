from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from api.models import User
# Create your tests here.


class RegisterationTests(APITestCase):
    def test_registration(self):
        url = reverse('register')
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword',
            'password2': 'testpassword'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LoginlogoutTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', 
                                             email='testuser@example.com',
                                               password='testpassword')
        self.logout_url = reverse('logout')
        
    def test_login(self):
        url = reverse('login')
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_logout(self):
        self.token = Token.objects.get(user__username='testuser')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(self.logout_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
