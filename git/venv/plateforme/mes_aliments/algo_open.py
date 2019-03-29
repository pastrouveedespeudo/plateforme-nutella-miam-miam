import sqlite3
import psycopg2


def image_aliment(para):

    conn = psycopg2.connect(database="plateforme",
                            user="postgres",
                            host="127.0.0.1",
                            password="tiotio")

                    
    cur = conn.cursor()
    
    cur.execute("""select image, name_aliment
                from public.mes_aliments_aliment
                where name_aliment = '{}';
                """.format(para))
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

    cur.execute("""SELECT name_aliment
                    FROM public.mes_aliments_aliment
                    WHERE name_aliment = '{}'""".format(para))
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


    cur.execute("""SELECT id_categorie_id
    FROM public.mes_aliments_aliment
    WHERE name_aliment = '{}'""".format(para))

    conn.commit()

    rows = cur.fetchall()
    
    indice_cat = [i[0] for i in rows]


    cur.execute("""SELECT name_aliment, id_categorie_id, nutriscore, image,id
    FROM public.mes_aliments_aliment
    WHERE name_aliment = '{}'""".format(para))

    conn.commit()

    rows = cur.fetchall()

    aliment_recherché = [i for i in rows]

    
    c = 0
    for i in indice_cat:
        
        cur.execute("""SELECT name_aliment, id_categorie_id, nutriscore, image,id
        FROM public.mes_aliments_aliment
        WHERE id_categorie_id = {} and nutriscore != 'No_found' and image != 'No_found'
        ORDER BY nutriscore ASC""".format(indice_cat[c]))

        conn.commit()
        
        rows = cur.fetchall()

        liste = [i for i in rows]

            
        c+=1


    liste = liste[:6]
    liste[0] = aliment_recherché[0]
   
    return liste



def detail_aliment(value):

    detail = []
    
    conn = psycopg2.connect(database="plateforme",
                            user="postgres",
                            host="127.0.0.1",
                            password="tiotio")

                
    cur = conn.cursor()

    cur.execute("""SELECT *
                    FROM public.mes_aliments_aliment
                    WHERE id = {}""".format(value))


    conn.commit()

    rows = cur.fetchall()

    detail = [i for i in rows]
  
    return detail



def replace(para):

    conn = psycopg2.connect(database="plateforme",
                            user="postgres",
                            host="127.0.0.1",
                            password="tiotio")

                
    cur = conn.cursor()


    cur.execute("""SELECT id_categorie_id
    FROM public.mes_aliments_aliment
    WHERE name_aliment = '{}'""".format(para))

    conn.commit()

    rows = cur.fetchall()
    
    indice_cat = [i[0] for i in rows]


    c = 0
    for i in indice_cat:
        
        cur.execute("""SELECT name_aliment, id_categorie_id, nutriscore, image,id
        FROM public.mes_aliments_aliment
        WHERE id_categorie_id = {} and nutriscore != 'No_found' and image != 'No_found'
        and name_aliment != '{}'
        ORDER BY nutriscore ASC""".format(indice_cat[c], para))

        conn.commit()
        
        rows = cur.fetchall()

        liste = [i for i in rows]

            
        c+=1


    liste = liste[:6]
 
   
    return liste



def data_replace(request, username, aliment, new_aliment):
    
    conn = psycopg2.connect(database="plateforme",
                            user="postgres",
                            host="127.0.0.1",
                            password="tiotio")

                
    cur = conn.cursor()
    print(aliment)
    print(new_aliment)
    print("GOGODANCEUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUR")
    
    cur.execute("""UPDATE aliment_de_{}
                set name_aliment = '{}' where name_aliment = '{}'
              


                """.format(username,  new_aliment, aliment))

    
    conn.commit()

        











    
