from django.shortcuts import render
from django.db import models
from .algo_open import *
import sqlite3
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .mes_aliments_user import *
from django.http import HttpResponse
from django.http import JsonResponse
from .mes_aliments_preferer_user import *


def aliment_det(request):
    
    if request.method == "POST":
        recherche = request.POST.get('produit')

        detail = detail_aliment(recherche)
        
        url_nutri = detail[0][4]
        aliment = detail[0][1]
        
        print(url_nutri,"YOOOOOOOOOOOOOOOOOOOOOOOOOOO")

        

        code = detail[0][2]
        image = detail[0][5]
        url_nutri = "/static/img/portfolio/nutriscore/" + str(detail[0][4]) + ".jpg >"
        
        return render(request, 'aliment_det.html',
                      {'detail':detail,
                       'url_nutri':url_nutri,
                       'code':code,
                       'image':image,
                       'aliment': aliment
                       })

    else:
        return render(request, 'aliment_det.html')

@csrf_exempt
def recherche(request):
                  
    liste_recherche = []
    stock_depassé = ""
    if request.method == "POST":

        recherche = request.POST.get('cool')
        username = request.POST.get('username')
        valider = request.POST.getlist('data[]')


        if valider and username:
            
            print("username : ",username,"recherche : ", valider)
            stock = controle_data_aliment(username)
            print(stock[1],"ajouter un produit")

            if stock[1] == True:
                insert_food(username, valider[0])
                
            elif stock[1] == False:
                
                stock_depassé = "oups vous avez trop d'aliment en stock supprime en ! ou remplace le !"
                
                print(stock_depassé)
        
        if recherche:
            current_user = request.user
            if current_user.is_authenticated:
                print(request.user.username)
                stock = controle_data_aliment(str(request.user.username))
                print(stock[1],"ajouter un produit")
                         
    
            print("etape recherche")
            image = image_aliment(recherche)
            titre = titre_aliment(recherche)
            a = better_nutri(recherche)
            
            return render(request, 'recherche.html',
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

                           "aaaa":"/static/img/portfolio/nutriscore/" + str(a[0][2]) + ".jpg >",
                           "bbbb":"/static/img/portfolio/nutriscore/" + str(a[1][2]) + ".jpg >",
                           "cccc":"/static/img/portfolio/nutriscore/" + str(a[2][2]) + ".jpg >",
                           "dddd":"/static/img/portfolio/nutriscore/" + str(a[3][2]) + ".jpg >",
                           "eeee":"/static/img/portfolio/nutriscore/" + str(a[4][2]) + ".jpg >",
                           "ffff":"/static/img/portfolio/nutriscore/" + str(a[5][2]) + ".jpg >",

                           "image":str(image[0][0]),
                           "titre":str(titre[0][0]),
                           "stock_depassé":stock_depassé,
                    
                           })

        
    image = '/static/img/header1.jpg'
    return render(request, 'recherche.html', {'image':image})




def mes_aliments(request):
    current_user = request.user

    food = mes_aliment_user(request.user.username)
    a = display_food(food)

    print(a[0][1],"122222222222222222222222222222222222222222222222221")


    return render(request, 'mes_aliments.html',
                  {"a":str(a[0][5]),
                   "b":str(a[1][5]),
                   "c":str(a[2][5]),
                   "d":str(a[3][5]),
                   "e":str(a[4][5]),
                   "f":str(a[5][5]),
                   
                   "aa":str(a[0][1]),
                   "bb":str(a[1][1]),
                   "cc":str(a[2][1]),
                   "dd":str(a[3][1]),
                   "ee":str(a[4][1]),
                   "ff":str(a[5][1]),
                   
                   "aaa":str(a[0][4]),
                   "bbb":str(a[1][4]),
                   "ccc":str(a[2][4]),
                   "ddd":str(a[3][4]),
                   "eee":str(a[4][4]),
                   "fff":str(a[5][4]),

                   "aaaa":"/static/img/portfolio/nutriscore/" + str(a[0][4]) + ".jpg >",
                   "bbbb":"/static/img/portfolio/nutriscore/" + str(a[1][4]) + ".jpg >",
                   "cccc":"/static/img/portfolio/nutriscore/" + str(a[2][4]) + ".jpg >",
                   "dddd":"/static/img/portfolio/nutriscore/" + str(a[3][4]) + ".jpg >",
                   "eeee":"/static/img/portfolio/nutriscore/" + str(a[4][4]) + ".jpg >",
                   "ffff":"/static/img/portfolio/nutriscore/" + str(a[5][4]) + ".jpg >",

          
            
                   })
























