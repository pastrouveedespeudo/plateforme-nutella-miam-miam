from django.test import TestCase
from django.urls import reverse


class indexpagetest(TestCase):
    
    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        

    def test_mention_page(self):
        response = self.client.get(reverse('mention'))
        self.assertEqual(response.status_code,200)
