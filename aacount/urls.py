from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
import os


urlpatterns = [
    path(r'', views.login),
    path(r'inscription', views.inscription),
    path(r'login', views.login),
    path(r'mon_compte', views.mon_compte),
    path(r'contact', views.contact),

    ]
