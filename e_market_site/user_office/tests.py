from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class UserOfficeViewTests(TestCase):
    def test_redirect_unathenticated_to_login(self):
        """
        Profile view redirect unathenticated users to login view
        """
        response = self.client.get(reverse('user_office:profile'))
        self.assertRedirects(response, reverse('accounts:login'))