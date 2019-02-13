from django.shortcuts import render



def mes_aliments(request):
    return render(request, 'pages/mes_aliments.html')

def recherche(request):
    return render(request, 'pages/recherche.html')
