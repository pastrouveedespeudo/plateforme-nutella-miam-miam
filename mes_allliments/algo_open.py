import sqlite3


class openfoodfact:

    def better_nutri(self):

        db = sqlite3.connect(r'C:\Users\jeanbaptiste\plateforme_nutella\plateforme_nutella\db.sqlite3')
        cursor = db.cursor()


        value = input("aliment ?")
        indice_cat = []
        

        cursor.execute('''SELECT id_categorie_id
        FROM mes_aliments_aliment
        WHERE name_aliment = (?)''',(value,))

        self.rows = cursor.fetchall()
        for i in self.rows:
            #print(i[0])
            indice_cat.append(i[0])

        print(indice_cat)


        c = 0
        for i in indice_cat:
            
            cursor.execute('''SELECT name_aliment, id_categorie_id, nutriscore
            FROM mes_aliments_aliment
            WHERE id_categorie_id = (?)
            ORDER BY nutriscore ASC''', (indice_cat[c],))

            db.commit()
            
            self.rows = cursor.fetchall()
            for i in self.rows:
                print(i)

            c+=1



       
yo = openfoodfact()
yo.better_nutri()
