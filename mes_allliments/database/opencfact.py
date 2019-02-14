from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import sqlite3




def openfactfood_database():
    
    db = sqlite3.connect(r'C:\Users\jeanbaptiste\plateforme_nutella\plateforme_nutella\db.sqlite3')
    cursor = db.cursor()
    
    liste = []

    path = "https://fr.openfoodfacts.org/categories"
    
    requete = requests.get(path)
    page = requete.content
    soup = BeautifulSoup(page, "html.parser")

    for tag in soup.find_all("td"):
        liste.append(tag.text)

    c = 0
    for i in range(3):
        print(liste[c])
        
        cursor.execute('''INSERT INTO mes_aliments_categorie(name_categorie) VALUES(?)''', (liste[c],))
        db.commit()
        c+=3

            
openfactfood_database()


