from django.shortcuts import render
from django.db import models
from .algo_open import *
import sqlite3



def aliment_det(request):
    
    if request.method == "POST":
        recherche = request.POST.get('produit')

        detail = detail_aliment(recherche)
        
        url_nutri = detail[0][4]

        
        print(url_nutri,"YOOOOOOOOOOOOOOOOOOOOOOOOOOO")

        

        code = detail[0][2]
        image = detail[0][5]
        
        return render(request, 'pages/aliment_det.html',
                      {'detail':detail,
                       'url_nutri':url_nutri,
                       'code':code,
                       'image':image,
                       })

    else:
        return render(request, 'pages/aliment_det.html')


def recherche(request):

    liste_recherche = []
    
    if request.method == "POST":

        recherche = request.POST.get('cool')
        print(recherche)

        image = image_aliment(recherche)
        titre = titre_aliment(recherche)
        a = better_nutri(recherche)
        
  

        

        return render(request, 'pages/recherche.html',
                      {"a":str(a[0][3]),
                       "b":str(a[1][3]),
                       "c":str(a[2][3]),
                       "d":str(a[3][3]),
                       "e":str(a[4][3]),
                       "f":str(a[5][3]),
                       
                       "aa":str(a[0][0]),
                       "bb":str(a[1][0]),
                       "cc":str(a[2][0]),
                       "dd":str(a[3][0]),
                       "ee":str(a[4][0]),
                       "ff":str(a[5][0]),
                       
                       "aaa":str(a[0][4]),
                       "bbb":str(a[1][4]),
                       "ccc":str(a[2][4]),
                       "ddd":str(a[3][4]),
                       "eee":str(a[4][4]),
                       "fff":str(a[5][4]),

                       "image":str(image[0][0]),
                       "titre":str(titre[0][0]),
                       })




























