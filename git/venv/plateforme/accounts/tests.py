from django.urls import reverse
from django.test import TestCase
from .models import *


class test_account(TestCase):
    
    def test_login_page(self):
        response = self.client.get(reverse('login_view'))
        self.assertEqual(response.status_code,200)

    def test_register_view_page(self):
        response = self.client.get(reverse('register_view'))
        self.assertEqual(response.status_code,200)

    def test_logout_view_page(self):
        response = self.client.get(reverse('logout_view'))
        self.assertEqual(response.status_code,302)

    def test_mon_compte_page(self):
        response = self.client.get(reverse('mon_compte'))
        self.assertEqual(response.status_code,302)

    def test_error_page(self):
        response = self.client.get(reverse('error'))
        self.assertEqual(response.status_code,200)


