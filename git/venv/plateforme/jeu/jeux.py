import sqlite3
import psycopg2
import random

def choix_aliment_niveau_1():

    conn = psycopg2.connect(database="plateforme",
                            user="postgres",
                            host="127.0.0.1",
                            password="tiotio")

                    
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
    print(aliment_nutri_a[0])

    three_other = []

    for i in range(3):
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
        three_other.append([i for i in rows])
        
    print(three_other)  
      


    return aliment_nutri_a[0], three_other









































