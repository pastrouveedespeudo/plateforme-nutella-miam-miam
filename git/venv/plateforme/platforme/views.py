from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):   
    return render(request, "home.html", {})

def mention(request):
    return render(request, "mention.html", {})

def handler404(request, exception, template_name="error.html"):
    return render(request, "error.html", {'message':'Page non trouvée'})

def handler500(request):
    return render(request, "error.html", {'message':'Erreur 505'})
