import psycopg2

def titre_aliment(para):

    conn = psycopg2.connect(database="plateforme",
                            user="postgres",
                            host="127.0.0.1",
                            password="tiotio")

                
    cur = conn.cursor()

    cur.execute("""SELECT name_aliment
                    FROM public.mes_aliments_aliment
                    WHERE name_aliment = '{}'""".format(para))
    conn.commit()
    
    rows = cur.fetchall()


    titre = [i for i in rows]
        
    print(titre,"123155555555555555555555555555555555555555")
    return titre

titre_aliment("Thé glacé Pêche")
