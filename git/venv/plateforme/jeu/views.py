from django.shortcuts import render
from .jeux import *
import random
from django.template.loader import render_to_string
from django.http import HttpResponse
import json as simplejson
from django.http import JsonResponse
from .verification_reponse import *
import random

def niveau1(message):

    un = choix_aliment_niveau_1()

    numero = ["1","2","3","4"]


    image = [str(un[0][2]), str(un[1][0][2]), str(un[1][1][2]), str(un[1][2][2])]

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


            
    data = {"image1":i, "image2":j,"image3":k,"image4":l,"yo":"coucou", 'message':message}

    return data



    
def niveau2(message):
    

    un = choix_aliment_niveau_2()

    numero = ["1","2","3","4","5","6","7","8"]

    image = [str(un[0][0]), str(un[1][0]), str(un[1][1]), str(un[1][2]), str(un[1][3]), str(un[1][4]),
             str(un[1][5]), str(un[1][6])]
    
    Ocontinuer = True
    while Ocontinuer:
    
        i = random.choice(image)
        j = random.choice(image)
        k = random.choice(image)
        l = random.choice(image)
        m = random.choice(image)
        n = random.choice(image)
        o = random.choice(image)
        p = random.choice(image)
        
        if i != j and i != k and i != l and i != m and i != n and i != o and i != p\
           and j != k and j != l and j != m and j != n and j != o and j != p\
           and k != l and k != m and k != n and k != m and k != n and k != p\
           and l != m and l != n and l != o and l != p\
           and m != n and m != n and m != o and m != p\
           and n != o and n != p\
           and o != p:
            Ocontinuer = False
            break
        else:
            j = l = k = l = m = n = o = p = ""

    
    data = {"image1":i, "image2":j,"image3":k,"image4":l,
            "image5":m, "image6":n,"image7":o,"image8":p, 'message':message}
  
    return data



        
def niveau1_continuer(continuer):
    
    liste = [[], []]
    c = 0
    for i in continuer:
        for j in i:
            if j == ',':
                c+=1
            else:
                liste[c].append(j)

    liste2 = []
    for i in liste:
        liste2.append("".join(i))
    

    liste10 = []
    food = aliment.objects.filter(image=str(liste2[1])).all()
    for i in food:
        liste10.append(i.nutriscore)

    for i in liste10:
        print(i)

    verif_nutri = liste10[0]

    if verif_nutri == "a":
        liste = ['bien joué', 'particpe a top chef', 'formidable']
        message = random.choice(liste)
    else:
        liste = ['nul']
        
        message = random.choice(liste)
        

    
    niv1 = niveau1(message)
    return niv1


def niveau2_continuer(continuer):
    
    liste = [[],[],[],[],[],[]]
    c=0
    for i in continuer:
        if i == ',':
            c+=1
        else:
            liste[c].append(i)

    liste = ["".join(i) for i in liste]

    

    
    print("l'utilisateur a choisis : ", liste[0])
    print("le produit est : ", liste[1])
    
    liste10 = []
    
    food_choose = aliment.objects.filter(image=liste[1]).all()
    
    for i in food_choose:
        liste10.append(i.nutriscore)

    for i in liste10:
        print(i)

    nutriscore_id = liste10[0]


    if nutriscore_id == "a":

        message = "oui bonne réponse"
    else:

        message = "non mauvaise réponse"
    
    a = niveau2(message)
    return a 

def jeux(request):

    current_user = request.user


    if request.method == "POST":

        niveau = request.POST.get('data')
        niveau = str(niveau)
  
        continuer = request.POST.get('data')
        continuer = str(continuer)

        current_user = request.user
 

        niveau_continuer = request.POST.get('data1')
     
        
        if niveau == "Niveau 1":
            lvl1 = niveau1('')
            return JsonResponse(lvl1)
        
        elif niveau == "Niveau 2":
            lvl2 = niveau2('')
            return JsonResponse(lvl2)

        elif niveau_continuer == "Niveau 2":
            lvl2_continue = niveau2_continuer(continuer)
            return JsonResponse(lvl2_continue)
        

        elif niveau_continuer == 'Niveau 1':
            lvl1_continue = niveau1_continuer(continuer)
            return JsonResponse(lvl1_continue)


    return render(request, "jeux.html")

































