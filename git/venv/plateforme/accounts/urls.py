from django.contrib import admin
from django.urls import path
from .views import essais, essais1, login, register_view

urlpatterns = [
    path('/essais', essais),
    path('/essais1', essais1),
    path('/login', login),
    path('/register_view', register_view),
    path('/logout_view', logout_view),
    ]
