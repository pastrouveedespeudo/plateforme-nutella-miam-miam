from django.shortcuts import render



def jeux(request):

    niveau1 = request.POST.get('niveau1')
    niveau2 = request.POST.get('niveau2')
    niveau3 = request.POST.get('niveau3')
    
    if niveau1:
        pass

    elif niveau2:
        pass

    elif niveau3:
        pass
       



    
    return render(request, "jeux.html", {}) 
