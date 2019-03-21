form = compte_utilisateur_form(request.POST or None)
    print(form)
    if form.is_valid():
        print("okiokioki")
        nom = form.cleaned_data['nom']
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']

        print("COUCOUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU")
        envoi = True


        if request.method == "POST":
            print("ohouiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
            email = request.POST.get('email')
            alita = inscription_email(email)
     
            form = compte_utilisateur_form(request.POST)

            
            if form.is_valid() and alita == []:
                
                nom = request.POST.get('nom')
                password = request.POST.get('password')
                email = request.POST.get('email')
            
                oobject = compte(nom=nom,
                                 
                                 password=password,
                                 email=email)
                oobject.save()

                return render(request, 'home.html',locals())
                #page recap inscription


            else:

                message="addresse mail deja utilisé"
                return render(request, 'pages/inscription.html', locals(), {'message':message})
                
    print("oyééééééééééééé")
    return render(request, 'pages/inscription.html',locals())

