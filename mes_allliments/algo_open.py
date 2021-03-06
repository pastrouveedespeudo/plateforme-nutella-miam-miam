import sqlite3

def image_aliment(para):

    image = []
    
    db = sqlite3.connect(r'C:\Users\jeanbaptiste\plateforme_nutella\plateforme_nutella\db.sqlite3')
    cursor = db.cursor()

    cursor.execute('''SELECT image, name_aliment
                    FROM mes_aliments_aliment
                    WHERE name_aliment = (?)''', (para,) )
    db.commit()
    
    rows = cursor.fetchall()


    for i in rows:
        image.append(i)
        

    return image

def titre_aliment(para):
    
    titre = []
    
    db = sqlite3.connect(r'C:\Users\jeanbaptiste\plateforme_nutella\plateforme_nutella\db.sqlite3')
    cursor = db.cursor()

    cursor.execute('''SELECT name_aliment
                    FROM mes_aliments_aliment
                    WHERE name_aliment = (?)''', (para,) )
    db.commit()
    
    rows = cursor.fetchall()


    for i in rows:
        titre.append(i)
        

    return titre



def better_nutri(para):

    liste = []

    db = sqlite3.connect(r'C:\Users\jeanbaptiste\plateforme_nutella\plateforme_nutella\db.sqlite3')
    cursor = db.cursor()

    indice_cat = []
    

    cursor.execute('''SELECT id_categorie_id
    FROM mes_aliments_aliment
    WHERE name_aliment = (?)''',(para,))

    db.commit()

    rows = cursor.fetchall()
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
    
    db = sqlite3.connect(r'C:\Users\jeanbaptiste\plateforme_nutella\plateforme_nutella\db.sqlite3')
    cursor = db.cursor()

    cursor.execute('''SELECT *
                    FROM mes_aliments_aliment
                    WHERE id = (?)''', (value,) )


    db.commit()

    rows = cursor.fetchall()
    for i in rows:
        detail.append(i)


    return detail





















    
