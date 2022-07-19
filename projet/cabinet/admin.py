from django.contrib import admin
from cabinet.models import Utilisateur, Patient, Disponibilite, RendezVous, DossierMedical

# Register your models here.

class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'cin', 'dateNaissance', 'numeroTelephone', 'sexe', 'adresse', 'salaire', 'email', 'motDePasse', 'role')  

admin.site.register(Utilisateur, UtilisateurAdmin)

class PatientAdmin(admin.ModelAdmin):  
    list_display = ('nom', 'prenom', 'cin', 'dateNaissance', 'numeroTelephone', 'sexe', 'adresse', 'profession', 'email', 'motDePasse')

admin.site.register(Patient, PatientAdmin) 

class DisponibiliteAdmin(admin.ModelAdmin):
    list_display = ('date', 'disponibilite')  

admin.site.register(Disponibilite, DisponibiliteAdmin)

class RendezVousAdmin(admin.ModelAdmin):  
    list_display = ('date', 'maladie', 'consultation', 'ordonnance', 'prix', 'prixTotal', 'modePaiement') 

admin.site.register(RendezVous, RendezVousAdmin) 

class DossierMedicalAdmin(admin.ModelAdmin):
    list_display = ('dateCreation', 'groupeSanguin', 'taille', 'poids', 'assuranceMaladie', 'allergies', 'vaccination')  

admin.site.register(DossierMedical, DossierMedicalAdmin)
