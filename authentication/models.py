from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    CREATEUR = "CREATEUR"
    ABONNE = "ABONNE"

    ROLE_CHOIX = (
        (CREATEUR, 'Créateur'),
        (ABONNE, "Abonné")
    )

    profile_photo = models.ImageField(verbose_name='Photo de profil')
    role = models.CharField(max_length=30, choices=ROLE_CHOIX)
