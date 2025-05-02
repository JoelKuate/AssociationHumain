from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_creation = models.DateTimeField(default=timezone.now)
    date_publication = models.DateTimeField(blank=True, null=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)

    def publier(self):
        self.date_publication = timezone.now()
        self.save()

    def __str__(self) -> str:
        return self.titre

    class Meta:
        ordering = ['-date_creation']


class Contact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    sujet = models.CharField(max_length=200)
    message = models.TextField()
    date_envoi = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.nom} - {self.sujet}"