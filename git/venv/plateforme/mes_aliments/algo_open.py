import psycopg2

def image_aliment(para):

    conn = psycopg2.connect(database="plateforme",
                            user="postgres",
                            host="127.0.0.1",
                            password="tiotio")

                    
    cur = conn.cursor()
    
    cur.execute('''SELECT image, name_aliment
                    FROM public.mes_aliments_aliment
                    WHERE name_aliment = "{0}"'''.format(para) )
    conn.commit()
    
    rows = cur.fetchall()

    image = [i for i in rows]

    return image

def titre_aliment(para):

    conn = psycopg2.connect(database="plateforme",
                            user="postgres",
                            host="127.0.0.1",
                            password="tiotio")

                
    cur = conn.cursor()

    cur.execute('''SELECT name_aliment
                    FROM public.mes_aliments_aliment
                    WHERE name_aliment = "{}"'''.format(para))
    conn.commit()
    
    rows = cur.fetchall()


    titre = [i for i in rows]
        

    return titre


def better_nutri(para):

    conn = psycopg2.connect(database="plateforme",
                            user="postgres",
                            host="127.0.0.1",
                            password="tiotio")

                
    cur = conn.cursor()


    cur.execute('''SELECT id_categorie_id
    FROM public.mes_aliments_aliment
    WHERE name_aliment = "{}"'''.format(para))

    conn.commit()

    rows = cur.fetchall()

    indice_cat = [i[0] for i in rows]


    #print(indice_cat)


    c = 0
    for i in indice_cat:
        
        cursor.execute('''SELECT name_aliment, id_categorie_id, nutriscore, image,id
        FROM public.mes_aliments_aliment
        WHERE id_categorie_id = {} and nutriscore != "None"
        ORDER BY nutriscore ASC'''.format(indice_cat[c]))

        db.commit()
        
        rows = cursor.fetchall()

        liste = [i for i in rows]

            
        c+=1


    liste = liste[:6]
    return liste



def detail_aliment(value):

    detail = []
    
    conn = psycopg2.connect(database="plateforme",
                            user="postgres",
                            host="127.0.0.1",
                            password="tiotio")

                
    cur = conn.cursor()

    cur.execute('''SELECT *
                    FROM public.mes_aliments_aliment
                    WHERE id = (?)''', (value,) )


    conn.commit()

    rows = cur.fetchall()

    detail = [i for i in rows]

    return detail





















    
