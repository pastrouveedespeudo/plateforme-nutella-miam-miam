from django import forms



class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    envoyeur = forms.EmailField(label="Votre adresse e-mail")
    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)


    nom = forms.CharField(max_length=255, label="")
    prenom = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)
    
    email = forms.EmailField(max_length=255)
    
    addresse = forms.CharField()
    ville = forms.CharField(max_length=255)
    code_postale = forms.CharField(max_length=255)
    
    sexe = forms.CharField(max_length=8)
    date = forms.CharField()
    statut = forms.CharField(max_length=255)




class compte_utilisateur(forms.Form):

    nom = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Nom',
                                                                        'justify':'center'}))

                    
    prenom = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'renom',
                                                                        'justify':'center'}))
    
    password = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Password',
                                                                        'justify':'center'}))
    
    email = forms.EmailField(max_length=255,widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                                        'justify':'center'}))
    
    addresse = forms.CharField(max_length=300,widget=forms.TextInput(attrs={'placeholder': 'Adresse',
                                                                            'size':'62'}))
    
    ville = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Ville',
                                                                        'justify':'center'}))
    
    code_postale = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Code postal',
                                                                        'justify':'center'}))
    
    sexe = forms.CharField(max_length=8, widget=forms.TextInput(attrs={'placeholder': 'Sexe',
                                                                        'justify':'center'}))
    
    date = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Date de naissance',
                                                                        'justify':'center'}))
    
    statut = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Statut',
                                                                        'justify':'center'}))













