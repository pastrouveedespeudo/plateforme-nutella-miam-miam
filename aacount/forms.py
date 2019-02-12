from django import forms


class compte_utilisateur_form(forms.Form):

    nom = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Nom',
                                                                        'justify':'center'}))

                    
    prenom = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'prenom',
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













