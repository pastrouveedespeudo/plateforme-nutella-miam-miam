"""This is functions for searching from database"""


from .config import DATABASE, USER, HOST, PASSWORD
from django.contrib.auth import get_user_model
from accounts.models import foodAccount

User = get_user_model()

def controle_data_food(username):
    """Here we watch if user have 6 products,
    if he has -6 we ask him to select products
    else we warned him to modify his selection"""

    u = User.objects.get(username=username)

    c = foodAccount()

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
    

    c = foodAccount()
    variable = ""

    verify2(c.name_aliment1, food_name, variable)
    verify2(c.name_aliment2, food_name, variable)
    verify2(c.name_aliment3, food_name, variable)
    verify2(c.name_aliment4, food_name, variable)
    verify2(c.name_aliment5, food_name, variable)
    verify2(c.name_aliment6, food_name, variable)
    


    variable2 = ""
    
    if variable == False:
        return ""

    else:
        print("yoooooooooooooooooooooooo")

##        verify3(c.name_aliment1, food_name, variable2, c)
##        verify3(c.name_aliment2, food_name, variable2, c)
##        verify3(c.name_aliment3, food_name, variable2, c)
##        verify3(c.name_aliment4, food_name, variable2, c)
##        verify3(c.name_aliment5, food_name, variable2, c)
##        verify3(c.name_aliment6, food_name, variable2, c)

        print(c.name_aliment1,"0000000000000000000000")
        print(c.name_aliment2,"0000000000000000000000")
        print(c.name_aliment3,"0000000000000000000000")
        print(c.name_aliment4,"0000000000000000000000")
        print(c.name_aliment5,"0000000000000000000000")
        print(c.name_aliment6,"0000000000000000000000")

def verify(data, liste):
    if data == "":
        pass
    else:
        number += 1

    

def verify2(data, food_name, variable):
    if data == food_name:
        variable =  False
    print(variable)

def verify3(data, food_name, variable, c):
    if data == "" and variable != False:
        data = food_name
        c.save()
        variable2 = False
    else:
        pass














