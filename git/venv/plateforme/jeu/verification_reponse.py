import psycopg2

def verification(aliment):
    
    conn = psycopg2.connect(database="plateforme",
                            user="postgres",
                            host="127.0.0.1",
                            password="tiotio")

                
    cur = conn.cursor()

    
    cur.execute("""select nutriscore, id
                    from mes_aliments_aliment
                    where image = '{}'""".format(aliment))

    
    conn.commit()

    
    rows = cur.fetchall()

    information = [i for i in rows]
    
    return information



def voir_aliment(id_aliment):

    
    conn = psycopg2.connect(database="plateforme",
                            user="postgres",
                            host="127.0.0.1",
                            password="tiotio")

                
    cur = conn.cursor()

    
    cur.execute("""select * from mes_aliments_aliment
                where id = {}""".format(id_aliment))

    
    conn.commit()

    
    rows = cur.fetchall()

    info_aliment = [i for i in rows]

    return info_aliment

























    
