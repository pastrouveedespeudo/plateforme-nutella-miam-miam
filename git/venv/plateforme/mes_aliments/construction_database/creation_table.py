"""Here we creating tables for our database"""

import psycopg2

class create_tables:

    def create_table_aliment(self):

        conn = psycopg2.connect(database="plateforme",
                                user="postgres",
                                host="127.0.0.1",
                                password="tiotio")

                    
        cur = conn.cursor()


        cur.execute("CREATE TABLE mes_aliments_aliment\
                    (id serial PRIMARY KEY,\
                    name_aliment VARCHAR(60) not null,\
                    code_product_food VARCHAR(40) not null,\
                    description TEXT not null,\
                    nutriscore VARCHAR(1) not null,\
                    image VARCHAR(100) not null,\
                    name_store VARCHAR(60) not null,\
                    name_brand VARCHAR(60) not null,\
                    id_categorie_id INT not null);")



        conn.commit()


    def create_table_substitut(self):
        conn = psycopg2.connect(database="plateforme",
                                user="postgres",
                                host="127.0.0.1",
                                password="tiotio")

                    
        cur = conn.cursor()


        cur.execute("CREATE TABLE mes_aliments_substitut\
                    (id serial PRIMARY KEY,\
                    name_aliment VARCHAR(60) not null,\
                    code_product_food VARCHAR(40) not null,\
                    description TEXT not null,\
                    nutriscore VARCHAR(1) not null,\
                    image VARCHAR(100) not null,\
                    name_store VARCHAR(60) not null,\
                    name_brand VARCHAR(60) not null,\
                    id_categorie_id INT not null);")



        conn.commit()

    def create_table_categorie(self):

        conn = psycopg2.connect(database="plateforme",
                                user="postgres",
                                host="127.0.0.1",
                                password="tiotio")

                    
        cur = conn.cursor()


        cur.execute("CREATE TABLE mes_aliments_categorie\
                    (id serial PRIMARY KEY,\
                    name_categorie VARCHAR(60) not null);")


        conn.commit()



    def create_table_recherche(self):

        conn = psycopg2.connect(database="plateforme",
                                user="postgres",
                                host="127.0.0.1",
                                password="tiotio")

                    
        cur = conn.cursor()


        cur.execute("CREATE TABLE mes_aliments_recherche\
                    (id serial PRIMARY KEY,\
                    recherche TEXT not null);")



        conn.commit()





if __name__ == "__main__":

    creation = create_tables()
                    
    creation.create_table_aliment()
    creation.create_table_substitut()
    creation.create_table_categorie()
    creation.create_table_recherche()




        
