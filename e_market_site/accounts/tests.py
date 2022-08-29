from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class LoginTest(TestCase):
    def test_can_access_page(self):
        response = self.client.get(reverse('accounts:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')