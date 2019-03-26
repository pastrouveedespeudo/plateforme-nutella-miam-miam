import sqlite3
import psycopg2


def image_aliment(para):

    image = []
    
    conn = psycopg2.connect(database="plateforme",
                            user="postgres",
                            host="127.0.0.1",
                            password="tiotio")

                    
    cur = conn.cursor()
    
    cur.execute('''SELECT image, name_aliment
                    FROM mes_aliments_aliment
                    WHERE name_aliment = {}'''.format(para) )
    conn.commit()
    
    rows = cur.fetchall()


    for i in rows:
        image.append(i)
        

    return image

def titre_aliment(para):
    
    titre = []
    
    conn = psycopg2.connect(database="plateforme",
                            user="postgres",
                            host="127.0.0.1",
                            password="tiotio")

                
    cur = conn.cursor()

    cur.execute('''SELECT name_aliment
                    FROM mes_aliments_aliment
                    WHERE name_aliment = (?)''', (para,) )
    conn.commit()
    
    rows = cur.fetchall()


    for i in rows:
        titre.append(i)
        

    return titre



def better_nutri(para):

    liste = []

    conn = psycopg2.connect(database="plateforme",
                            user="postgres",
                            host="127.0.0.1",
                            password="tiotio")

                
    cur = conn.cursor()

    indice_cat = []
    

    cur.execute('''SELECT id_categorie_id
    FROM mes_aliments_aliment
    WHERE name_aliment = (?)''',(para,))

    conn.commit()

    rows = cur.fetchall()
    for i in rows:
        indice_cat.append(i[0])

    #print(indice_cat)


    c = 0
    for i in indice_cat:
        
        cursor.execute('''SELECT name_aliment, id_categorie_id, nutriscore, image,id
        FROM mes_aliments_aliment
        WHERE id_categorie_id = (?) and nutriscore != "None"
        ORDER BY nutriscore ASC''', (indice_cat[c],))

        db.commit()
        
        rows = cursor.fetchall()
        for i in rows:
            #print(i)
            liste.append(i)

            
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
                    FROM mes_aliments_aliment
                    WHERE id = (?)''', (value,) )


    conn.commit()

    rows = cur.fetchall()
    for i in rows:
        detail.append(i)


    return detail





















    
