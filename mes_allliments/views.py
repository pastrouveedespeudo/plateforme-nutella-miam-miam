from django.shortcuts import render
from django.db import models
import requests
from bs4 import BeautifulSoup
import json

from .models import categorie

def mes_aliments(request):
            

            
    return render(request, 'pages/mes_aliments.html')

def recherche(request):
    return render(request, 'pages/recherche.html')
































