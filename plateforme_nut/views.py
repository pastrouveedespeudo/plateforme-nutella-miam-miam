from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def mes_aliments(request):
    return render(request, 'pages/mes_aliments.html')


