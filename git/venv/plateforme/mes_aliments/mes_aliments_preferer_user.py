"""Here we discuss with database for
food from user database"""

import psycopg2
from .config import DATABASE, USER, HOST, PASSWORD
from accounts.models import *

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
 
    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 
    cur = conn.cursor()
    liste_ali = []
    try:
        for i in liste_aliment:
            cur.execute("""SELECT distinct name_aliment,
                        code_product_food,description,nutriscore,
                        image,name_store,name_brand
                        FROM public.mes_aliments_aliment
                        where LOWER(name_aliment) = '{}'
                        """.format(i))
            conn.commit()

            rows = cur.fetchall()
            for i in rows:
                liste_ali.append(i)
        c=0

        return liste_ali

    except:
        pass
