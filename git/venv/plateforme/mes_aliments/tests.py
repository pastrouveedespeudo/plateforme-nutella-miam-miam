from django.urls import reverse
from django.test import TestCase
from .models import *

class test_aliment(TestCase):


    def test_mes_aliments_page(self):
        
        response = self.client.get(reverse('mes_aliments'))
        self.assertEqual(response.status_code,200)


    def test_recherche_page(self):
        response = self.client.get(reverse('recherche'))
        self.assertEqual(response.status_code,200)


    def test_aliment_det_page(self):
        response = self.client.get(reverse('aliment_det'))
        self.assertEqual(response.status_code,200)

        

        
    def test_remplacement_page(self):
        response = self.client.get(reverse('remplacement'))
        self.assertEqual(response.status_code,200)

        

        
