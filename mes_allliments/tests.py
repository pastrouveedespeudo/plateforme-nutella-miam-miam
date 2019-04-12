from django.urls import reverse
from django.test import TestCase
from .models import *

class test_page_aliment(TestCase):

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

        
class test_aliment(TestCase):
    
    def test_categorie(self):
        cat = categorie.objects.create(name_categorie='legume')

        category_name = categorie.objects.get(id=1)
        out = category_name.name_categorie
        out1 = category_name.id
        
        self.assertEqual(out, 'legume')
        self.assertEqual(out1, 1)

        
    def test_image(self):


        cat = categorie.objects.create(id=1,
                                       name_categorie='legume')
        
        food = aliment.objects.create(name_aliment='carotte',
                                      code_product_food='4649849',
                                      description='caroote',
                                      nutriscore='a',
                                      image='htps://carotte.com',
                                      name_store='marché',
                                      name_brand='marché',
                                      id_categorie_id=1)
        
        food_search = aliment.objects.get(name_aliment='carotte')
        out = food_search.image

        self.assertEqual(out, 'htps://carotte.com')





    def title(self):
        pass


































