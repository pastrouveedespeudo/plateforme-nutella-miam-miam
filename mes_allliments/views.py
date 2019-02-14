from django.shortcuts import render
from django.db import models


def mes_aliments(request):     
    return render(request, 'pages/mes_aliments.html')

def recherche(request):

    
    
    if request.method == "POST":
        print("choubaCHOUBAAAAAAAAAAAAA")
        print(request.POST.get('cool'))

        return render(request, 'pages/recherche.html')































