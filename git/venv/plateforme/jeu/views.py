from django.shortcuts import render
from .jeux import *
import random


def jeux(request):
    if request.method == "POST":
        print("ouiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
        niveau = request.POST.get('data')
        niveau = str(niveau)
        print(niveau,"00000000000000000000")
    
        if niveau == "Niveau 1":
            print("niveauuuuuuuuuuuuuuuuuuuuu 1")
            un = choix_aliment_niveau_1()


            numero = ["1","2","3","4"]
            image = [un[0][2], un[1][0][0][2], un[1][1][0][2], un[1][2][0][2]]

            continuer = True
            while continuer:
                print("en cours")
                i = random.choice(image)
                j = random.choice(image)
                k = random.choice(image)
                l = random.choice(image)
                if i != j and i != k and i != l\
                   and j != k and j != l\
                   and k != l:
                    continuer = False
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

            return render(request, 'jeux.html', {"image1":i,
                                                "image2":j,
                                                "image3":k,
                                                "image4":l,
                                                 'yo':'coucouuu
                                                })




        
        elif niveau == "Niveau 2":
            pass

        elif niveau == "Niveau 3":
            pass
           



    
    return render(request, "jeux.html", {}) 
