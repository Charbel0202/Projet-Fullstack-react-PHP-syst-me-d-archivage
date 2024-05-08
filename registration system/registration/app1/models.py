from django.db import models
from django.contrib.auth.models import User

class Utilisateur(models.Model):
    idUtilisateur = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    pseudo = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.nom
