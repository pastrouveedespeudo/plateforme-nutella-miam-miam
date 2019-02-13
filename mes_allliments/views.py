from django.shortcuts import render
from django.db import models
import requests
from bs4 import BeautifulSoup
import json

from .models import categorie

def mes_aliments(request):
            

            
    return render(request, 'pages/mes_aliments.html')

def recherche(request):
    return render(request, 'pages/recherche.html')


def openfactfood_database(request):

    
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
        objet = categorie(name_categorie = liste[c])
        objet.save()
        c+=3
    return render(request, 'pages/openfactfood_database.html')





























