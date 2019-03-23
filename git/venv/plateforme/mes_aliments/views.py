from django.shortcuts import render

def mes_aliments(request):
    return render(request, "mes_aliments.html", {}) 



def recherche(request):
    return render(request, "recherche.html", {}) 
