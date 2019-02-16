from django import forms

from django.contrib.auth import (
    authenticate,
    get_user_model
    )

user = get_user_model()

class compte_utilisateur_form(forms.Form):

    nom = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Nom'}))

                    
    prenom = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'prenom'}))
    
    password = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Password'}))
    
    email = forms.EmailField(max_length=255,widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    
    addresse = forms.CharField(max_length=300,widget=forms.TextInput(attrs={'placeholder': 'Adresse'}))
    
    ville = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Ville'}))
    
    code_postale = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Code postal'}))
    
    sexe = forms.CharField(max_length=8, widget=forms.TextInput(attrs={'placeholder': 'Sexe'}))
    
    date = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Date de naissance'}))
    
    statut = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Statut'}))




class userloginform(forms.Form):
    
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    

    def clean(self, *args, **kwargs):

        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                raise forms.ValidationError('non existing')

            if not user.check_password(password):
                raise forms.ValidationError('non password biatch')

            if not user.is_active:
                raise forms.ValidationError('non active')

        return super(userloginform, self).clean(*args, **kwargs)




class userregisterform(forms.ModelForm):

    
    email = forms.EmailField(label="Email adresse")
    email2 = forms.EmailField(label="Email adresse")
    password = forms.CharField(widget=forms.PasswordInput)



    class mera:
        model = user
        fields =[
            'username',
            'email',
            'email2',
            'password',

            ]


    def clean_email(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')

        if email != email2:
            raise forms.ValidationError("pas les meme")

        email_qs = user.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("existe deja rton email")

        return email
    
        




































