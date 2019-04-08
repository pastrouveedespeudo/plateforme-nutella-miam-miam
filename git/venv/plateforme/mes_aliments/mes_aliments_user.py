"""This is functions for searching from database"""


from .config import DATABASE, USER, HOST, PASSWORD
from django.contrib.auth import get_user_model
from accounts.models import food_account

User = get_user_model()

def controle_data_food(username):
    """Here we watch if user have 6 products,
    if he has -6 we ask him to select products
    else we warned him to modify his selection"""

    u = User.objects.get(username=username)

    c = food_account()

    number = 0
    
    verify(c.name_aliment1, number)
    verify(c.name_aliment2, number)
    verify(c.name_aliment3, number)
    verify(c.name_aliment4, number)
    verify(c.name_aliment5, number)
    verify(c.name_aliment6, number)

 
    if number >= 6:
        return "nombre de produit suppérieur a 6", False
    
    else:
        return "stockage du produit possible", True


def insert_food(username, food_name):
    """He we insert food"""

    u = User.objects.get(username=username)
    
    c = food_account()
    variable = ""
    
    verify2(c.name_aliment1, food_name, variable)
    verify2(c.name_aliment2, food_name, variable)
    verify2(c.name_aliment3, food_name, variable)
    verify2(c.name_aliment4, food_name, variable)
    verify2(c.name_aliment5, food_name, variable)
    verify2(c.name_aliment6, food_name, variable)

    if variable == False:
        return ""

    else:
        verify3(c.name_aliment1, food_name)
        verify3(c.name_aliment2, food_name)
        verify3(c.name_aliment3, food_name)
        verify3(c.name_aliment4, food_name)
        verify3(c.name_aliment5, food_name)
        verify3(c.name_aliment6, food_name)



def verify(data, liste):
    if data == "":
        pass
    else:
        number += 1

    

def verify2(data, food_name, variable):
    if data == food_name:
        variable =  False


def verify3(data, food_name):
    if data == "":
        data = food_name
    else:
        pass














