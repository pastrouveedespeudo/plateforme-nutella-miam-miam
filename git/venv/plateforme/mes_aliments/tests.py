from django.urls import reverse
from django.test import TestCase
from .models import *

class test_aliment(TestCase):


    def test_mes_aliments_page(self):
        response = self.client.get(reverse('mes_aliments'))
        self.assertEqual(response.status_code,200)


    
##    def test_num1(self):
##        
##        categorie1 = categorie.objects.create(name_categorie='fruit')
##        
##        aliment1 = aliment.objects.create(
##            name_aliment = 'orange',
##            code_product_food = '231348',
##            description = 'orange',
##            nutriscore = 'a',
##            image = 'https://orange.com',
##            name_store = 'orange',
##            name_brand = 'orange',
##            id_categorie = categorie1
##
##            )
##
##        aliment2 = aliment.objects.create(
##            name_aliment = 'fraise',
##            code_product_food = '11111',
##            description = 'fraise',
##            nutriscore = 'a',
##            image = 'https://fraise.com',
##            name_store = 'fraise',
##            name_brand = 'fraise',
##            id_categorie = categorie1
##            )
##        
##        aliment3 = aliment.objects.create(
##            name_aliment = 'tomate',
##            code_product_food = '22222',
##            description = 'tomate',
##            nutriscore = 'a',
##            image = 'https://tomate.com',
##            name_store = 'tomate',
##            name_brand = 'tomate',
##            id_categorie = categorie1
##            )
##        
##        aliment4 = aliment.objects.create(
##            name_aliment = 'giwi',
##            code_product_food = '3333',
##            description = 'giwi',
##            nutriscore = 'a',
##            image = 'https://giwi.com',
##            name_store = 'giwi',
##            name_brand = 'giwi',
##            id_categorie = categorie1
##            )
##        
##        aliment5 = aliment.objects.create(
##            name_aliment = 'pamplemousse',
##            code_product_food = '444444',
##            description = 'pamplemousse',
##            nutriscore = 'a',
##            image = 'https://pamplemousse.com',
##            name_store = 'pamplemousse',
##            name_brand = 'pamplemousse',
##            id_categorie = categorie1
##            )
##        
##        aliment6 = aliment.objects.create(
##        
##            name_aliment = 'citron',
##            code_product_food = '55555',
##            description ='citron',
##            nutriscore = 'a',
##            image = 'https://citron.com',
##            name_store = 'citron',
##            name_brand = 'citron',
##            id_categorie = categorie1
##            )
##
##        al1 = aliment.objects.get(name_aliment='orange').id
##        al2 = aliment.objects.get(name_aliment='fraise').id
##        al3 = aliment.objects.get(name_aliment='tomate').id
##        al4 = aliment.objects.get(name_aliment='giwi').id
##        al5 = aliment.objects.get(name_aliment='pamplemousse').id
##        al6 = aliment.objects.get(name_aliment='citron').id
##
##        response = self.client.get(reverse('mes_aliments:mes_aliments',
##                                   args=(al1,)))
##
##        self.assertEqual(response.status_code, 200)


##
##
##    def test_num2(self):
##        categorie1 = categorie.objects.create(name_categorie='fruit')
##
##        aliment1 = aliment.objects.create(
##            name_aliment = 'orange',
##            code_product_food = '231348',
##            description = 'orange',
##            nutriscore = 'a',
##            image = 'https://orange.com',
##            name_store = 'orange',
##            name_brand = 'orange',
##            id_categorie = categorie1
##
##            )
##
##        aliment2 = aliment.objects.create(
##            name_aliment = 'fraise',
##            code_product_food = '11111',
##            description = 'fraise',
##            nutriscore = 'a',
##            image = 'https://fraise.com',
##            name_store = 'fraise',
##            name_brand = 'fraise',
##            id_categorie = categorie1
##            )
##        
##        aliment3 = aliment.objects.create(
##            name_aliment = 'tomate',
##            code_product_food = '22222',
##            description = 'tomate',
##            nutriscore = 'a',
##            image = 'https://tomate.com',
##            name_store = 'tomate',
##            name_brand = 'tomate',
##            id_categorie = categorie1
##            )
##        
##        aliment4 = aliment.objects.create(
##            name_aliment = 'giwi',
##            code_product_food = '3333',
##            description = 'giwi',
##            nutriscore = 'a',
##            image = 'https://giwi.com',
##            name_store = 'giwi',
##            name_brand = 'giwi',
##            id_categorie = categorie1
##            )
##        
##        aliment5 = aliment.objects.create(
##            name_aliment = 'pamplemousse',
##            code_product_food = '444444',
##            description = 'pamplemousse',
##            nutriscore = 'a',
##            image = 'https://pamplemousse.com',
##            name_store = 'pamplemousse',
##            name_brand = 'pamplemousse',
##            id_categorie = categorie1
##            )
##        
##        aliment6 = aliment.objects.create(
##        
##            name_aliment = 'citron',
##            code_product_food = '55555',
##            description ='citron',
##            nutriscore = 'a',
##            image = 'https://citron.com',
##            name_store = 'citron',
##            name_brand = 'citron',
##            id_categorie = categorie1
##            )
##
##        al1 = aliment.objects.get(name_aliment='orange').id 
##        al2 = aliment.objects.get(name_aliment='fraise').id 
##        al3 = aliment.objects.get(name_aliment='tomate').id
##        al4 = aliment.objects.get(name_aliment='giwi').id 
##        al5 = aliment.objects.get(name_aliment='pamplemousse').id 
##        al6 = aliment.objects.get(name_aliment='citron').id 
##
##        response = self.client.get(reverse('mes_aliments:mes_aliments'),
##                                   args=(al1,al2,al3,
##                                         al4,al5,al6,))
##
##        self.assertEqual(response.status_code, 404)
##
##












        
