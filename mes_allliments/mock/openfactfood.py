from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import sqlite3
import json


class data:

    
    def categorie(self):
 
        db = sqlite3.connect(r'C:\Users\jeanbaptiste\plateforme_nutella\plateforme_nutella\db.sqlite3')
        cursor = db.cursor()
        
        self.liste = []

        path = "https://fr.openfoodfacts.org/categories"
        
        requete = requests.get(path)
        page = requete.content
        soup = BeautifulSoup(page, "html.parser")

        for tag in soup.find_all("td"):
            self.liste.append(tag.text)

        c = 0
        for i in range(3):
            print(self.liste[c])
            
            cursor.execute('''INSERT INTO mes_aliments_categorie(name_categorie) VALUES(?)''', (self.liste[c],))
            db.commit()
            c+=3


    def insert_food(self):
        """Here we run api and we take informations necessary for tables insertion"""

        db = sqlite3.connect(r'C:\Users\jeanbaptiste\plateforme_nutella\plateforme_nutella\db.sqlite3')
        cursor = db.cursor()

        
        c = 0
        d = 1
        self.liste_store = []
        self.liste_store1 = [[], [], [], [], [], [], [], [],
                             [], [], [], [], [], [], [], [],
                             [], [], [], [], [], [], [], []]
        
        self.liste_brands = []
        self.liste_brands1 = [[], [], [], [], [], [], [], [],
                              [], [], [], [], [], [], [], [],
                              [], [], [], [], [], [], [], []]
        
        
        self.liste2 = []
        
        for i in range(3):

            print(self.liste[c])
            print("\n")
            
            path2 = "https://fr.openfoodfacts.org/categorie/{}".format(self.liste[c])
            requete = requests.get(path2)
            page = requete.content
            soup = BeautifulSoup(page, "html.parser")
            for tag in soup.find_all("span"):
                self.liste2.append(tag.text)

            for i in self.liste2[6:]:
                print(i)
                a = str(i).find(" - ")
                i = i[0:a]
                print(i)
                path3 = "https://fr.openfoodfacts.org/cgi/search.pl?search_terms={}&json=1"
                search = path3.format(i)
                r = requests.get(search)
                data = json.loads(r.text)
                
                try:
                    self.number_product = data["products"][0]['code']
                except:
                    self.number_product = "None"
                try:
                    self.description_product = data["products"][0]["ingredients_text_fr"]
                except:
                    self.description_product = "None"
               
                try:
                    self.nutriscore = data["products"][0]["nutrition_grades"]
                except:
                    self.nutriscore = "None"

                try:
                    self.image = data["products"][0]["image_front_url"]
                except:
                    self.image = "None"


                cursor.execute("""
                INSERT INTO mes_aliments_aliment (name_aliment, code_product_food,
                description, nutriscore, image, id_categorie_id)
                VALUES(?,?,?,?,?,?)""", (i, self.number_product, self.description_product, self.nutriscore, self.image, d) )
       
                db.commit()
                
 
            d+=1
            c+=3
            self.liste2 = []


def insert_brand(self):
    pass











yo = data()           
yo.categorie()
yo.insert_food()

