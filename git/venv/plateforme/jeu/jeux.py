import sqlite3
import psycopg2
import random
from .config import *
from mes_aliments.models import *

def choix_aliment_niveau_1():

    choice = aliment.objects.all().filter(nutriscore='a')
    food = random.choice(choice)
    name = food.name_aliment
    nutri = food.nutriscore
    picture = food.image

    liste_food_a = [name, nutri, picture]


    liste = []
    choice2 = aliment.objects.all().exclude(nutriscore='a')
    for i in choice2:
        liste.append((i.name_aliment, i.nutriscore, i.image))

    un = random.choice(liste)
    liste.remove(un)
    deux = random.choice(liste)
    liste.remove(deux)
    trois = random.choice(liste)

    
    liste_3_not_a = [un, deux, trois]

    return liste_food_a, liste_3_not_a


def choix_aliment_niveau_2():

    conn = psycopg2.connect(database=DATABASE,
                                user=USER,
                                host=HOST,
                                password=PASSWORD)                    
    cur = conn.cursor()
    
    nutriscore = {}

    cur.execute("""SELECT name_aliment, nutriscore,
                image
                from public.mes_aliments_aliment
                where nutriscore = 'a' and name_aliment != 'No_found' and
                image != 'No_found'
                order by random()
                limit 1;
                """)

    rows = cur.fetchall()
    aliment_nutri_a = [i for i in rows]
 

    seven_other = []

    for i in range(7):
        cur.execute("""SELECT name_aliment, nutriscore,
                    image
                    from public.mes_aliments_aliment
                    where nutriscore != 'a' and name_aliment != 'No_found' and
                    image != 'No_found'
                    order by random()
                    limit 1;
                    """)
        
        conn.commit()

        rows = cur.fetchall()
        seven_other.append([i for i in rows])
        


    return aliment_nutri_a[0], seven_other





































