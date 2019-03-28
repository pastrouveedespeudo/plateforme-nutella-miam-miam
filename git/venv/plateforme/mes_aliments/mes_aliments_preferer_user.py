import psycopg2

def mes_aliment_user(username):


    
    conn = psycopg2.connect(database="plateforme",
                            user="postgres",
                            host="127.0.0.1",
                            password="tiotio")
          
    cur = conn.cursor()

    cur.execute("""SELECT * FROM aliment_de_{0}
                """.format(username))

    conn.commit()

    rows = cur.fetchall()
    food_user = [i for i in rows]

    food = [i[1] for i in food_user[1:]]
  
    return food

def display_food(liste_aliment):
    print(liste_aliment)

    conn = psycopg2.connect(database="plateforme",
                            user="postgres",
                            host="127.0.0.1",
                            password="tiotio")
          
    cur = conn.cursor()

    liste_ali = []

    for i in liste_aliment:
        cur.execute("""SELECT * FROM public.mes_aliments_aliment
                    where name_aliment = '{}'
                    """.format(i))

        conn.commit()
        

        rows = cur.fetchall()
        for i in rows:
            liste_ali.append(i)


    return liste_ali

























