import sqlite3

def inscription(para):

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

    print(liste)

    return liste


def loggin(self):
    pass



inscription("fe@hotmail.fr")
