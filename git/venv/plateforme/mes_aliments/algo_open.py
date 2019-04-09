"""Here we discuss with database"""
import psycopg2
from .config import DATABASE, USER, HOST, PASSWORD
from .models import aliment
from django.db import connection
from accounts.models import foodAccount
from django.db.models.functions import Lower

def image_aliment(para):
    """Here we search food picture """

    try:
        food = aliment.objects.get(name_aliment__contains='{}'.format(para))
        food = aliment.objects.get(name_aliment=para)
        image = food.image
        return image
    
    except:
        para = para.split()
        food = aliment.objects.get(name_aliment__contains=str(para[0]))
        image = food.image
        return image

    
def titre_aliment(para):
    """Here we search title picture """
    try:
        food = aliment.objects.get(name_aliment=para)
        title = food.name_aliment
        return title
    
    except:
        para = para.split()
        food = aliment.objects.get(name_aliment__contains=str(para[0]))
        title = food.name_aliment
        return title
   

def better_nutri(para):
    """Here we search best nutriscore from category
    from food search"""

    food = aliment.objects.get(name_aliment=para)
    aliment_recherché = [food.name_aliment, food.id_categorie_id,
                        food.nutriscore, food.image, food.id]
  
    category = aliment.objects.filter(id_categorie_id=food.id_categorie_id)

    liste = []

    count = 0
    for i in category:
        if count == 20:
            break
        else:
            a = []
            a = [i.name_aliment, i.id_categorie_id,
                 i.nutriscore, i.image]
            liste.append(a)
    
        count += 1


    liste = liste[:6]
    liste[0] = aliment_recherché

    return liste


def food_details(value):
    """Here we calling informations about product. Thank to that we
    can redirect to Openfactfood"""

    details = aliment.objects.get(image='{}'.format(value))

    return details



def replace(para):
    """We replace food from my_food"""
    
    para = para.lower()
    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()

    cur.execute("""SELECT id_categorie_id
    FROM public.mes_aliments_aliment
    WHERE LOWER(name_aliment) = '{}'""".format(para))

    conn.commit()
    rows = cur.fetchall()
    indice_cat = [i[0] for i in rows]
    indice_cat = indice_cat[0]

    c = 0
    for i in range(20):
        
        cur.execute("""SELECT distinct LOWER(name_aliment), id_categorie_id, nutriscore, image
        FROM public.mes_aliments_aliment
        WHERE id_categorie_id = {} and nutriscore != 'No_found' and image != 'No_found'
        and LOWER(name_aliment) != '{}'
        ORDER BY nutriscore ASC""".format(indice_cat, para))

        conn.commit()
        rows = cur.fetchall()
        liste = [i for i in rows]
            
        c+=1

    liste = set(liste)
    liste = list(liste)
    liste = liste[:6]
 
    return liste


def data_replace(request, username, aliment, new_aliment):
    """ """   


    
    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)                
    cur = conn.cursor()

    cur.execute("""UPDATE aliment_de_{}
                set name_aliment = '{}' where LOWER(name_aliment) = '{}'
                """.format(username,  new_aliment, aliment))

    
    conn.commit()


def verification_product_not_two(username, produit):
    """here we check that the food is not already present"""

    c = foodAccount.objects.get(name=username)
    if c.name_aliment1 == produit or c.name_aliment2  == produit or\
       c.name_aliment3  == produit or c.name_aliment4  == produit or\
       c.name_aliment5  == produit or c.name_aliment1  == produit:
        return False    
    else:
        return True


def verification_remplacement(username, produit):
    """We verify food isnt already present""" 

    c = foodAccount.objects.get(name=username)

    food = [c.name_aliment1, c.name_aliment2, c.name_aliment3,
            c.name_aliment4, c.name_aliment5, c.name_aliment6]


    for i in food:
        if produit == i:
            print("produit deja dans")
            return False
    print("pas produit deja !")
    return True

    


