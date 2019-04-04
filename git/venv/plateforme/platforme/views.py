from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.http import Http500

def home(request):   
    return render(request, "home.html", {})

def mention(request):
    return render(request, "mention.html", {})

def handler404(request):
    return render(request, "error.html", {}, statut=404)

def handler500(request):
    return render(request, "error.html", {}, statut=500)
