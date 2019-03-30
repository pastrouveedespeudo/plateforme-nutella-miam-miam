import psycopg2
#a cahng"
def verification(aliment):
    
    conn = psycopg2.connect(database="plateforme",
                            user="postgres",
                            host="127.0.0.1",
                            password="tiotio")

                
    cur = conn.cursor()

    
    cur.execute("""select nutriscore
                    from mes_aliments_aliment
                    where image = '{}'""".format(aliment))

    
    conn.commit()

    
    rows = cur.fetchall()

    information = [i for i in rows]

    print('le nutriscore bella est de : ', information)
    print("verification(), verification_reponse.py") 
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


    print("voir_aliment(), verification_reponse.py")


    return info_aliment

























    
