from django.shortcuts import render
from .jeux import *
import random
from django.template.loader import render_to_string
from django.http import HttpResponse
import json as simplejson
from django.http import JsonResponse

def jeux(request):
   
    if request.method == "POST":


        niveau = request.POST.get('data')
        niveau = str(niveau)
  
        continuer = request.POST.get('data')
        
        if niveau == "Niveau 1":
            print('Choix de niveau: niveau 1')
            un = choix_aliment_niveau_1()


            numero = ["1","2","3","4"]
            image = [un[0][2], un[1][0][0][2], un[1][1][0][2], un[1][2][0][2]]

            continuer = True
            while continuer:
            
                i = random.choice(image)
                j = random.choice(image)
                k = random.choice(image)
                l = random.choice(image)
                if i != j and i != k and i != l\
                   and j != k and j != l\
                   and k != l:
                    continuer = False
                    break
                else:
                    j = l = k = ""
                    
            print('fini')
            print(i)
            print("\n")
            print(j)
            print("\n")
            print(k)
            print("\n")
            print(l)
            print("\n")

            data = {"image1":i, "image2":j,"image3":k,"image4":l,"yo":"coucou"}
            print(data)
            return JsonResponse(data)



        
        elif niveau == "Niveau 2":
            pass

        elif niveau == "Niveau 3":
            pass
           

        elif continuer:
            print('ouiiiiiiiiiiiiiiii')
            un = choix_aliment_niveau_1()
            numero = ["1","2","3","4"]
            image = [un[0][2], un[1][0][0][2], un[1][1][0][2], un[1][2][0][2]]

            continuer = True
            while continuer:
            
                i = random.choice(image)
                j = random.choice(image)
                k = random.choice(image)
                l = random.choice(image)
                if i != j and i != k and i != l\
                   and j != k and j != l\
                   and k != l:
                    continuer = False
                    break
                else:
                    j = l = k = ""
                    
            data = {"image1":i, "image2":j,"image3":k,"image4":l}
            print(data)
            return JsonResponse(data)


            
    return render(request, "jeux.html", {}) 


































