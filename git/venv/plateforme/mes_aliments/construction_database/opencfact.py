"""Here we insert data into our database from api openfactfood"""

from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import json
import psycopg2


class data:

    
    def categorie(self):

        conn = psycopg2.connect(database="plateforme",
                                user="postgres",
                                host="127.0.0.1",
                                password="tiotio")

        cursor = conn.cursor()
        
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
            
            self.liste[c] = self.liste[c].replace(" ", "_")
            self.liste[c]= self.liste[c].replace("'", "")
            
            cursor.execute("INSERT INTO mes_aliments_categorie(name_categorie) VALUES ('{0}')".format(str(self.liste[c])))
            conn.commit()
            c+=3


    def insert_food(self):
        """Here we run api and we take informations necessary for tables insertion"""

        conn = psycopg2.connect(database="plateforme",
                                user="postgres",
                                host="127.0.0.1",
                                password="tiotio")

        cursor = conn.cursor()
 

        
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
                    print("nutriscore=",self.nutriscore)
                except:
                    self.nutriscore = "None"

                try:
                    self.image = data["products"][0]["image_front_url"]
                except:
                    self.image = "None"


                try:
                    self.brandss = data["products"][0]["brands"]
                    if self.brandss == '':
                        self.liste_brands.append(self.brandss)
                    else:
                        self.liste_brands.append(self.brandss)
                except:
                    self.brandss = "None"
                    self.liste_brands.append("None")



                try:
                    self.store_product = data["products"][0]["stores"]
                    if self.store_product == '':
                        self.liste_store.append("None")
                    else:
                        self.liste_store.append(self.store_product)
                except:
                    self.store_product = "None"
                    self.liste_store.append("None")


                print(i)
                print("\n")
                print(self.number_product)
                print("\n")
                print(self.description_product)
                print("\n")
                print(self.nutriscore)
                print("\n")
                print(self.image)
                print("\n")
                print(d)
                print("\n")
                print(self.store_product)
                print("\n")
                print(self.brandss)

                
                self.liste[c]= self.liste[c].replace("'", " ")
                
                cursor.execute("INSERT INTO mes_aliments_aliment (name_aliment)\
                                VALUES('{0}');".format(i))

                cursor.execute("INSERT INTO mes_aliments_aliment (image)\
                                VALUES('{0}');".format(self.image))

            
                cursor.execute("INSERT INTO mes_aliments_aliment (code_product_food)\
                                VALUES('{0}');".format(self.number_product))


                cursor.execute("INSERT INTO mes_aliments_aliment (description)\
                                VALUES('{0}');".format(self.description_product))

                cursor.execute("INSERT INTO mes_aliments_aliment (nutriscore)\
                                VALUES('{0}');".format(self.nutriscore))





                cursor.execute("INSERT INTO mes_aliments_aliment (id_categorie_id)\
                                VALUES('{0}');".format(d))

                cursor.execute("INSERT INTO mes_aliments_aliment (name_store)\
                                VALUES('{0}')".format(self.store_product))


                cursor.execute("INSERT INTO mes_aliments_aliment (name_brand)\
                                VALUES('{0}');".format(self.brandss))

       
                conn.commit()


                
 
            d+=1
            c+=3
            self.liste2 = []


                                                












yo = data()           
yo.categorie()
yo.insert_food()

