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
    
    c = foodAccount.objects.get(name=username)

  
    if c.name_aliment1 == "":
        c.name_aliment1 = food_name
        c.save()
        
    elif c.name_aliment2 == "":
        c.name_aliment2 = food_name
        c.save()
        
    elif c.name_aliment3 == "":
        c.name_aliment3 = food_name
        c.save()
        
    elif c.name_aliment4 == "":
        c.name_aliment4 = food_name
        c.save()
        
    elif c.name_aliment5 == "":
        c.name_aliment5 = food_name
        c.save()
        
    elif c.name_aliment6 == "":
        c.name_aliment6 = food_name
        c.save()
    
    else:
        print("trop d'aliment")

    print(c.name_aliment1)
    print(c.name_aliment2)
    print(c.name_aliment3)
    print(c.name_aliment4)
    print(c.name_aliment5)
    print(c.name_aliment6)


 
def verify(data, liste):
    if data == "":
        pass
    else:
        number += 1
    

def verify2(data, food_name, variable):
    print(data, food_name)
    if data == food_name:
        print("ouiiiiiiiiiiiiiii")
        variable =  False
    print(variable)

def verify3(data, food_name, variable, c, food):
    if data == "" and variable != False:
        data = '{}'.format(food_name)

        
        c.save()



        
        variable2 = False
    else:
        pass














