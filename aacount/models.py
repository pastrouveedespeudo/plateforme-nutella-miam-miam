from django.db import models

class compte(models.Model):

    nom = models.CharField(max_length=255)
            
    prenom = models.CharField(max_length=255)
    
    password = models.CharField(max_length=255)
    
    email = models.EmailField(max_length=255)
    
    addresse = models.CharField(max_length=300)
    
    ville = models.CharField(max_length=255)
                             
    code_postale = models.CharField(max_length=255)
                                    
    sexe = models.CharField(max_length=8)
                            
    date = models.CharField(max_length=10)
    
    statut = models.CharField(max_length=255)

    def __str__(self):
        return self.email
