from django.shortcuts import render
from django.db import models
from .algo_open import *
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .mes_aliments_user import *
from django.http import HttpResponse
from django.http import JsonResponse
from .mes_aliments_preferer_user import *
from django.shortcuts import redirect

def aliment_det(request):
    message=''
    if request.method == "POST":
  
        recherche = request.POST.get('produit')
      
       
        detail = detail_aliment(recherche)

        url_nutri = detail[0][3]
        aliment = detail[0][1]
        
        #on recherche selon l'aliment et on redef l'url nutri et aliment
     

        

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
            current_user = request.user
        
            stock = controle_data_aliment(username)


            if stock[1] == True:
                veri = verification_produit_pas_deux_fois(current_user,
                                                          valider[0])
                print(veri)
                if veri == True:
                    insert_food(username, valider[0])
                    print("aliment pas deja")
            elif stock[1] == False:
                print('aliment deja')
                stock_depassé = "oups vous avez trop d'aliment en stock supprime en ! ou remplace le !"
                
      
        
        if recherche:
            
            current_user = request.user
            if current_user.is_authenticated:
           
                stock = controle_data_aliment(str(request.user.username))
             
                 
                if stock[1] == False:
                    stock_depassé = "oups vous avez trop d'aliment en stock supprime en ! ou remplace le !"
                
     
            image = image_aliment(recherche)
            titre = titre_aliment(recherche)
            try:
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
                               
                               "aaa":str(a[0][3]),
                               "bbb":str(a[1][3]),
                               "ccc":str(a[2][3]),
                               "ddd":str(a[3][3]),
                               "eee":str(a[4][3]),
                               "fff":str(a[5][3]),

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
            
            except:
                #lentille verte -> lentillex/a6verte
                message = "oups nous n'avons pas cet aliment en database"
                return render(request, 'error.html', {"message":message})
        
    image = '/static/img/header1.jpg'
    return render(request, 'recherche.html', {'image':image})




def mes_aliments(request):
    current_user = request.user

  
    
    food = mes_aliment_user(request.user.username)
    a = display_food(food)

    try:
        return render(request, 'mes_aliments.html',
                      {"a":str(a[0][4]),
                       "b":str(a[1][4]),
                       "c":str(a[2][4]),
                       "d":str(a[3][4]),
                       "e":str(a[4][4]),
                       "f":str(a[5][4]),
                       
                       "aa":str(a[0][0]),
                       "bb":str(a[1][0]),
                       "cc":str(a[2][0]),
                       "dd":str(a[3][0]),
                       "ee":str(a[4][0]),
                       "ff":str(a[5][0]),


                       "aaaa":"/static/img/portfolio/nutriscore/" + str(a[0][3]) + ".jpg >",
                       "bbbb":"/static/img/portfolio/nutriscore/" + str(a[1][3]) + ".jpg >",
                       "cccc":"/static/img/portfolio/nutriscore/" + str(a[2][3]) + ".jpg >",
                       "dddd":"/static/img/portfolio/nutriscore/" + str(a[3][3]) + ".jpg >",
                       "eeee":"/static/img/portfolio/nutriscore/" + str(a[4][3]) + ".jpg >",
                       "ffff":"/static/img/portfolio/nutriscore/" + str(a[5][3]) + ".jpg >",

                       "aaaaa":str(a[0][0]),
                       "bbbbb":str(a[1][0]),
                       "ccccc":str(a[2][0]),
                       "ddddd":str(a[3][0]),
                       "eeeee":str(a[4][0]),
                       "fffff":str(a[5][0]),

              
                
                       })
    except:
        message = "Veuillez remplir votre selection d'aliment de 6 produit svp =) "
        return render(request, 'error.html', {"message":message})

def remplacement(request):
    message = ''


    if request.method == "POST":

        
        replace_it = request.POST.getlist('remplace_food')
    
        
        if replace_it:
            print(replace_it)
            print("oui")
            current_user = request.user
            b = verification_remplacement(current_user, replace_it[0])
            
            liste = [[],[]]
            element = []
            c=0
            for i in replace_it:
                for j in i:
                    if j == ",":
                        c+=1
                    else:
                        liste[c].append(j)
                c+=1
            for i in liste:
                i = "".join(i)
                element.append(i)
            if b == False:
                data_replace(request, current_user,
                             element[0], element[1]
                             )
            else:
                message = 'vous avez deja cet aliment'
                
        else:
            print("nan")
            
            aliment = request.POST.get('rem')
    
            current_user = request.user

            image = image_aliment(aliment)
            titre = titre_aliment(aliment)
            
            a = replace(str(aliment))
                
            

            return render(request, 'remplacement.html',
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
                           
                           "aaa":str(a[0][3]),
                           "bbb":str(a[1][3]),
                           "ccc":str(a[2][3]),
                           "ddd":str(a[3][3]),
                           "eee":str(a[4][3]),
                           "fff":str(a[5][3]),

                           "aaaa":"/static/img/portfolio/nutriscore/" + str(a[0][2]) + ".jpg >",
                           "bbbb":"/static/img/portfolio/nutriscore/" + str(a[1][2]) + ".jpg >",
                           "cccc":"/static/img/portfolio/nutriscore/" + str(a[2][2]) + ".jpg >",
                           "dddd":"/static/img/portfolio/nutriscore/" + str(a[3][2]) + ".jpg >",
                           "eeee":"/static/img/portfolio/nutriscore/" + str(a[4][2]) + ".jpg >",
                           "ffff":"/static/img/portfolio/nutriscore/" + str(a[5][2]) + ".jpg >",

                           "image":str(image[0][0]),
                           "titre":str(titre[0][0]),
                           'message':message
                    
                           })

            
    current_user = request.user

    food = mes_aliment_user(request.user.username)
    a = display_food(food)
      
    return render(request, 'mes_aliments.html',
                  {"a":str(a[0][4]),
                   "b":str(a[1][4]),
                   "c":str(a[2][4]),
                   "d":str(a[3][4]),
                   "e":str(a[4][4]),
                   "f":str(a[5][4]),
                   
                   "aa":str(a[0][0]),
                   "bb":str(a[1][0]),
                   "cc":str(a[2][0]),
                   "dd":str(a[3][0]),
                   "ee":str(a[4][0]),
                   "ff":str(a[5][0]),


                   "aaaa":"/static/img/portfolio/nutriscore/" + str(a[0][3]) + ".jpg >",
                   "bbbb":"/static/img/portfolio/nutriscore/" + str(a[1][3]) + ".jpg >",
                   "cccc":"/static/img/portfolio/nutriscore/" + str(a[2][3]) + ".jpg >",
                   "dddd":"/static/img/portfolio/nutriscore/" + str(a[3][3]) + ".jpg >",
                   "eeee":"/static/img/portfolio/nutriscore/" + str(a[4][3]) + ".jpg >",
                   "ffff":"/static/img/portfolio/nutriscore/" + str(a[5][3]) + ".jpg >",

                   "aaaaa":str(a[0][0]),
                   "bbbbb":str(a[1][0]),
                   "ccccc":str(a[2][0]),
                   "ddddd":str(a[3][0]),
                   "eeeee":str(a[4][0]),
                   "fffff":str(a[5][0]),
                   'message':message
          
            
                   })


def error(request):
    return render(request, "error.html")














