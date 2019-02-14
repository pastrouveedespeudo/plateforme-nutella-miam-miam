from django.shortcuts import render
from django.db import models
from .algo_open import *
import sqlite3

def mes_aliments(request):     
    return render(request, 'pages/mes_aliments.html')

def recherche(request):

    liste_recherche = []
    
    if request.method == "POST":

        recherche = request.POST.get('cool')
        print(recherche)
        a = better_nutri(recherche)
        #print(a[0][3])
        print(a)
        




        
        return render(request, 'pages/recherche.html',
                      {"a":str(a[0][3]),
                       "b":str(a[1][3])})































