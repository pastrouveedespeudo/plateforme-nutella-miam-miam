import psycopg2


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
