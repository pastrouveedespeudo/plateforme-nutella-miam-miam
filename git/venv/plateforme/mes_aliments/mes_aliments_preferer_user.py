"""Here we discuss with database for
food from user database"""

import psycopg2
from .config import DATABASE, USER, HOST, PASSWORD
from accounts.models import *
from mes_aliments.models import *


def mes_aliment_user(username):
    """Here we take user food"""

    c = foodAccount.objects.get(name=username)
    food = [c.name_aliment1, c.name_aliment2, c.name_aliment3,
            c.name_aliment4, c.name_aliment5, c.name_aliment6]
    for i in food:
        print(i)
    return food

def display_food(liste_aliment):
    """Here we take informations food for template"""

    

   
    liste_ali = []
    try:
        for i in liste_aliment:
             z = aliment.objects.get(name_aliment=i)
             liste = []
             liste = [z.name_aliment, z.code_product_food,
                      z.description, z.nutriscore,
                      z.image, z.name_store, z.name_brand]

             liste_ali.append(liste)
     

        return liste_ali
    
    except:
        pass
     
