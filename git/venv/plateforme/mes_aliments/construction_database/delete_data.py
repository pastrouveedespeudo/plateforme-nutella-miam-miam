from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import psycopg2


class delete:

    def delete_data_categorie(self):
        
        conn = psycopg2.connect(database="plateforme",
                                user="postgres",
                                host="127.0.0.1",
                                password="tiotio")

        cursor = conn.cursor()
        
        cursor.execute('''DELETE FROM mes_aliments_categorie''')
        conn.commit()

        print("categori supprimer gros, c la seul chose qui marche pour l'instant ")
    

    def delete_data_aliment(self):
        
        conn = psycopg2.connect(database="plateforme",
                                user="postgres",
                                host="127.0.0.1",
                                password="tiotio")

        cursor = conn.cursor()
        
        cursor.execute('''DELETE FROM mes_aliments_aliment''')
        conn.commit()

        print("aliment supprimer hihihi")

    def delete_tables_aliment(self):
        
        conn = psycopg2.connect(database="plateforme",
                                user="postgres",
                                host="127.0.0.1",
                                password="tiotio")

        cursor = conn.cursor()
        
        cursor.execute('''DROP TABLE mes_aliments_aliment''')
        conn.commit()

        print("database supprimer hihihi")

    def delete_tables_categorie(self):
        
        conn = psycopg2.connect(database="plateforme",
                                user="postgres",
                                host="127.0.0.1",
                                password="tiotio")

        cursor = conn.cursor()
        
        cursor.execute('''DROP TABLE mes_aliments_categorie''')
        conn.commit()

        print("database supprimer hihihi")


    def delete_tables_store(self):
        
        conn = psycopg2.connect(database="plateforme",
                                user="postgres",
                                host="127.0.0.1",
                                password="tiotio")

        cursor = conn.cursor()
        
        cursor.execute('''DROP TABLE mes_aliments_store''')
        conn.commit()

        print("database supprimer hihihi")


    def delete_tables_brand(self):
        
        conn = psycopg2.connect(database="plateforme",
                                user="postgres",
                                host="127.0.0.1",
                                password="tiotio")

        cursor = conn.cursor()
        
        cursor.execute('''DROP TABLE mes_aliments_brand''')
        conn.commit()

        print("database supprimer hihihi")


yo = delete()
yo.delete_data_categorie()
yo.delete_data_aliment()
#yo.delete_tables_brand()
#yo.delete_tables_aliment()
#yo.delete_tables_store()
#yo.delete_tables_categorie()
