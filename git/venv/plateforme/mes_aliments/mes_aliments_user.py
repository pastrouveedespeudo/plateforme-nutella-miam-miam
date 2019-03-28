import psycopg2


def controle_data_aliment(username):
    
    conn = psycopg2.connect(database="plateforme",
                            user="postgres",
                            host="127.0.0.1",
                            password="tiotio")

                
    cur = conn.cursor()


    cur.execute("""SELECT COUNT(name_aliment) FROM aliment_de_{0}
                    """.format(username))

    conn.commit()

    rows = cur.fetchall()

    count_food = [i for i in rows]
    print(count_food[0][0],"fooooooooooooooooooooooooooooooooooooooood")
    if count_food[0][0] >= 6:
        return "nombre de produit suppérieur a 6", False
    
    else:
        return "stockage du produit possible", True


def insert_food(username, food_name):
    
    conn = psycopg2.connect(database="plateforme",
                            user="postgres",
                            host="127.0.0.1",
                            password="tiotio")

                
    cur = conn.cursor()



    cur.execute("""INSERT INTO aliment_de_{0}
                    (name_aliment)
                    VALUES ('{1}');
                );""".format(username, food_name))



    conn.commit()
