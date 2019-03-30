from django.shortcuts import render
from .jeux import *
import random
from django.template.loader import render_to_string
from django.http import HttpResponse
import json as simplejson
from django.http import JsonResponse
from .score import *
from .verification_reponse import *


def jeux(request):

    current_user = request.user
    point = score(current_user)

   
    if request.method == "POST":


        niveau = request.POST.get('data')
        niveau = str(niveau)
  
        continuer = request.POST.get('data')
        continuer = str(continuer)

        current_user = request.user
        point = score(current_user)

        
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


            liste = [[],[]]
            c=0
            for i in continuer:
                if i == ',':
                    c+=1
                else:
                    liste[c].append(i)

            liste = ["".join(i) for i in liste]

            
            print(liste)
            
            print("l'utilisateur a choisis : ", liste[0])
            print("le produit est : ", liste[1])
            
            current_user = request.user
            
            nutriscore_id = verification(liste[1])
            print(nutriscore_id[0][0],"0000000000000000000000000000000000000000")

            if nutriscore_id[0][0] == "a":
                update_score(request.user, 5)
                print("oui bonne réponse + 5")
                message = "oui bonne réponse + 5"
            else:
                print("non mauvaise réponse")
                message = "non mauvaise réponse"
            
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
                    
            data = {"image1":i, "image2":j,"image3":k,"image4":l,"message":message}
            DATA = []
            return JsonResponse(data)


            
    return render(request, "jeux.html", {'score':point}) 


































