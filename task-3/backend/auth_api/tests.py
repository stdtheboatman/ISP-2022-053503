import json
from django.test import TestCase
from django.contrib.auth.models import User
from .views import RegisterView

from rest_framework.test import APIRequestFactory
# Create your tests here.
class AuthTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="exist_name", password="123")

    def test_register_exist_username(self):
        factory = APIRequestFactory()
        request = factory.post('api/register/', {'username': 'exist_name', 'password': 'fsadjfnasdkjnfasdjkfnasjkdnf123', 'password2': 'fsadjfnasdkjnfasdjkfnasjkdnf123'})
        
        response = RegisterView(request)
        
        self.assertNotEqual(response.status_code, 200)
        
    def test_register_ok(self):
        factory = APIRequestFactory()
        request = factory.post('/', {"username": "random_name", "password": "fsadjfnasdkjnfasdjkfnasjkdnf123", "password2": "fsadjfnasdkjnfasdjkfnasjkdnf123"}, format='json')
        
        response = RegisterView(request)
        
        self.assertEqual(response.status_code, 200)
        
    def test_register_easy_password(self):
        factory = APIRequestFactory()
        request = factory.post('/', {"username": "random_name", "password": "123", "password2": "123"}, format='json')
        
        response = RegisterView(request)
        
        self.assertNotEqual(response.status_code, 200)
        
    def test_register_not_equals_passwords(self):
        factory = APIRequestFactory()
        request = factory.post('/', {"username": "random_name", "password": "fsadjfnasdkjnfasdjkfnasjkdnf123456", "password2": "fsadjfnasdkjnfasdjkfnasjkdnf123"}, format='json')
        
        response = RegisterView(request)
        self.assertNotEqual(response.status_code, 200)
        
        