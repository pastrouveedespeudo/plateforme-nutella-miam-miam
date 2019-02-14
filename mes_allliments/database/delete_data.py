from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import sqlite3


class delete:

    def delete_data_categorie(self):
        db = sqlite3.connect(r'C:\Users\jeanbaptiste\plateforme_nutella\plateforme_nutella\db.sqlite3')
        cursor = db.cursor()
        
        cursor.execute('''DELETE FROM mes_aliments_categorie''')
        db.commit()

        print("categori supprimer gros, c la seul chose qui marche pour l'instant ")
    

    def delete_data_aliment(self):
        db = sqlite3.connect(r'C:\Users\jeanbaptiste\plateforme_nutella\plateforme_nutella\db.sqlite3')
        cursor = db.cursor()
        
        cursor.execute('''DELETE FROM mes_aliments_aliment''')
        db.commit()

        print("aliment supprimer hihihi")

    def delete_tables_aliment(self):
        
        db = sqlite3.connect(r'C:\Users\jeanbaptiste\plateforme_nutella\plateforme_nutella\db.sqlite3')
        cursor = db.cursor()
        
        cursor.execute('''DROP TABLE mes_aliments_aliment''')
        db.commit()

        print("database supprimer hihihi")

    def delete_data_categorie(self):
        
        db = sqlite3.connect(r'C:\Users\jeanbaptiste\plateforme_nutella\plateforme_nutella\db.sqlite3')
        cursor = db.cursor()
        
        cursor.execute('''DROP TABLE mes_aliments_categorie''')
        db.commit()

        print("database supprimer hihihi")


    def delete_tables_store(self):
        
        db = sqlite3.connect(r'C:\Users\jeanbaptiste\plateforme_nutella\plateforme_nutella\db.sqlite3')
        cursor = db.cursor()
        
        cursor.execute('''DROP TABLE mes_aliments_store''')
        db.commit()

        print("database supprimer hihihi")


    def delete_tables_brand(self):
        
        db = sqlite3.connect(r'C:\Users\jeanbaptiste\plateforme_nutella\plateforme_nutella\db.sqlite3')
        cursor = db.cursor()
        
        cursor.execute('''DROP TABLE mes_aliments_brand''')
        db.commit()

        print("database supprimer hihihi")


yo =delete()
yo.delete_data_categorie()
yo.delete_data_aliment()
yo.delete_tables_brand()
yo.delete_tables_aliment()
yo.delete_tables_store()
yo.delete_tables_categorie()
