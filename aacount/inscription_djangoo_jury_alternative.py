    print(request)

    next = request.GET.get('next')
    form = userloginform(request.POST or None)
 
    if form.is_valid():
        print("validddddddddddddddddddddddd")
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        print(username, password,"000000000000000000000000000000000000000")
        user = authenticate(username=username, password=password)

        lo(request, user)

        if next:
            return redirect(next)
        return redirect("/")

    
    context = {
        'form':form,

        }
    
        
    return render(request, 'pages/login.html', context)
