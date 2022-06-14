from django.test import TestCase
from .models import User
from .views import setUserData
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient

# Create your tests here.
class ApiTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="test_user", password="123")

    def test_set_user_data_bad_data(self):
        client = APIClient()
        client.login(username="test_user", password="123")
        
        response = client.post("api/setUserData/", {"apiKey: 123", "secretKey1111: 123"}, format="json")
        
        self.assertNotEqual(response.status_code, 200)