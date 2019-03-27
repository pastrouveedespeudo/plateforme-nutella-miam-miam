from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
    )

from .database_utilisateur import *


from .forms import UserLoginForm, UserRegisterForm



@login_required
def mon_compte(request):
    return render(request, "mon_compte.html", {}) 



def essais(request):
    return render(request, "essais.html", {})

@login_required
def essais1(request):
    return render(request, "essais1.html", {})



def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form':form
    }

    return render(request, 'login.html', context)




def register_view(request):
    
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    
    if form.is_valid():

        user = form.save(commit=False)

        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()

        create_database_user(user.username)
        insert_database_user(user.username)
        new_user = authenticate(username=user.username, password=password)

        login(request, new_user)
        
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form':form
    }

    return render(request, 'signup.html', context)


login_required
def logout_view(request):
    logout(request)
    print("déconnexion")
    return redirect('/')

















    
