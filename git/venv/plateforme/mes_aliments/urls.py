from django.contrib import admin
from django.urls import path
from .views import mes_aliments
from .views import recherche



urlpatterns = [
    path('/mes_aliments', mes_aliments),
    path('/recherche', recherche),



    ]
