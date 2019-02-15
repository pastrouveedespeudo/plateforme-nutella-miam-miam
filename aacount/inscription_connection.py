import sqlite3

def inscription_email(para):

    liste = []
 
    db = sqlite3.connect(r'C:\Users\jeanbaptiste\plateforme_nutella\plateforme_nutella\db.sqlite3')
    cursor = db.cursor()

    cursor.execute('''SELECT *
                    FROM account_compte
                    WHERE email = (?)''', (para,) )
    
    db.commit()

    rows = cursor.fetchall()


    for i in rows:
        liste.append(i)


    return liste


def loggin(para):

    identifiant = []

    db = sqlite3.connect(r'C:\Users\jeanbaptiste\plateforme_nutella\plateforme_nutella\db.sqlite3')
    cursor = db.cursor()


    cursor.execute('''SELECT nom, password
                    FROM account_compte
                    WHERE nom = (?)''', (para,) )
    
    db.commit()

    rows = cursor.fetchall()


    for i in rows:
        identifiant.append(i)

    print(identifiant,"0000000000084987498749748974998")
    return identifiant
    



















