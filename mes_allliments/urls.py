from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
import os
from django.conf.urls import include


urlpatterns = [
    path(r'aliment_det', views.aliment_det),
    path(r'recherche', views.recherche),
    path(r'mes_aliments', views.mes_aliments),
    ]
