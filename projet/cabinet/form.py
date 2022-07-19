from django import forms
#from django.forms import TextInput
from cabinet.models import Utilisateur, Patient, Disponibilite, RendezVous, DossierMedical

class PatientForm(forms.ModelForm):
   class Meta:
     model = Patient
     fields = '__all__'

class UtilisateurForm(forms.ModelForm):
   class Meta:
     model = Utilisateur
     fields = '__all__'

class DossierMedicalForm(forms.ModelForm):
   class Meta:
     model = DossierMedical
     fields = '__all__'

class RendezVousForm(forms.ModelForm):
   class Meta:
     model = RendezVous
     fields = '__all__'

class DisponibiliteForm(forms.ModelForm):
   class Meta:
     model = Disponibilite
     fields = '__all__'