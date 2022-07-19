from django.db import models

from asyncio.windows_events import NULL
from datetime import datetime
from django.core.validators import MinValueValidator

# Create your models here.

class Utilisateur(models.Model):

    def __str__(self):
        return f'{self.nom} {self.prenom}'
    
    nom = models.fields.CharField(max_length=20, null=False)
    prenom = models.fields.CharField(max_length=20, null=False)
    cin = models.fields.CharField(max_length=20, null=False)
    dateNaissance = models.fields.DateField(null=True, blank=True)
    numeroTelephone = models.fields.CharField(max_length=20, null=False)
    sexe = models.fields.CharField(max_length=20, null=False)
    adresse = models.fields.CharField(max_length=200, null=False)
    salaire = models.fields.FloatField(validators=[MinValueValidator(0)],null=True,blank=True)
    email = models.fields.EmailField(max_length=100, null=False)
    motDePasse = models.fields.CharField(max_length=100, null=False)
    role = models.fields.CharField(max_length=20, null=False)

class Patient(models.Model):

    def __str__(self):
        return f'{self.nom} {self.prenom}'

    nom = models.fields.CharField(max_length=20, null=False)
    prenom = models.fields.CharField(max_length=20, null=False)
    cin = models.fields.CharField(max_length=20, null=False)
    dateNaissance = models.fields.DateField(null=True, blank=True)
    numeroTelephone = models.fields.CharField(max_length=20, null=False)
    sexe = models.fields.CharField(max_length=20, null=False)
    adresse = models.fields.CharField(max_length=200, null=False)
    profession = models.fields.CharField(max_length=100, null=False)
    email = models.fields.EmailField(max_length=100, null=False)
    motDePasse = models.fields.CharField(max_length=100, null=False)

class Disponibilite(models.Model):

    def __str__(self):
        return f'{self.date} | {self.utilisateur} | {self.disponibilite}'

    date = models.fields.DateTimeField(null=True)
    disponibilite = models.fields.BooleanField(default=False)

    utilisateur = models.ForeignKey(Utilisateur, null=True, blank=True, on_delete=models.SET_NULL)

class RendezVous(models.Model):

    def __str__(self):
        return f' {self.patient}  | {self.utilisateur} | {self.date}'

    date = models.fields.DateTimeField(null=False)
    maladie =  models.fields.CharField(max_length=100, null=False)
    consultation =  models.fields.CharField(max_length=1000, null=False)
    ordonnance =  models.fields.CharField(max_length=2000, null=False)
    prix = models.fields.FloatField(validators=[MinValueValidator(0)],null=True,blank=True)
    prixTotal = models.fields.FloatField(validators=[MinValueValidator(0)],null=False)
    modePaiement = models.fields.CharField(max_length=1000, null=False)

    patient = models.ForeignKey(Patient, null=True, blank=True, on_delete=models.SET_NULL)
    utilisateur = models.ForeignKey(Utilisateur, null=True, blank=True, on_delete=models.SET_NULL)

class DossierMedical(models.Model):

    def __str__(self):
        return f'{self.patient} {self.dateCreation}'

    dateCreation = models.fields.DateTimeField(null=True, blank=True)
    groupeSanguin = models.fields.CharField(max_length=5, null=False)
    taille = models.fields.FloatField(validators=[MinValueValidator(0)],null=False)
    poids = models.fields.FloatField(validators=[MinValueValidator(0)],null=False)
    assuranceMaladie = models.fields.CharField(max_length=500, null=False)
    allergies = models.fields.CharField(max_length=2000, null=True, blank=True)
    vaccination = models.fields.CharField(max_length=2000, null=False)

    patient = models.ForeignKey(Patient, null=True, blank=True, on_delete=models.SET_NULL)

