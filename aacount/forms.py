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

    nom = forms.CharField(max_length=255)
    prenom = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)
    
    email = forms.EmailField(max_length=255)
    
    addresse = forms.CharField()
    ville = forms.CharField(max_length=255)
    code_postale = forms.CharField(max_length=255)
    
    sexe = forms.CharField(max_length=8)
    date = forms.CharField()
    statut = forms.CharField(max_length=255)


