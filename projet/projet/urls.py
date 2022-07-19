"""projet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cabinet import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accueil/',views.accueil_index, name='accueil-index'),
    path('accueill/',views.accueill_index, name='accueill-index'),
    path('contact/',views.contact_index, name='contact-index'),
    path('statistique/',views.statistique, name='statistique'),
    path('facture/',views.facture, name='facture'),

    path('logout/', views.logout, name='logout'),
    path('login/',views.login, name='login'),
    path('register/',views.register, name='register'),
    path('registerr/',views.registerr, name='registerr'),
    
    path('patients/', views.patient_index, name='patient-index'),
    path('patients/<int:id>', views.patient_detail, name="patient-detail"), 
    path('patients/<int:id>/change/', views.patient_update, name="patient-update"),
    path('patients/<int:id>/delete/', views.patient_delete, name="patient-delete"),
    path('patients/add/', views.patient_create, name="patient-create"),

    path('utilisateurs/', views.utilisateur_index, name='utilisateur-index'),
    path('utilisateurs/<int:id>', views.utilisateur_detail, name="utilisateur-detail"), 
    path('utilisateurs/<int:id>/change/', views.utilisateur_update, name="utilisateur-update"),
    path('utilisateurs/<int:id>/delete/', views.utilisateur_delete, name="utilisateur-delete"),
    path('utilisateurs/add/', views.utilisateur_create, name="utilisateur-create"),

    path('dossierMedicals/', views.dossier_index, name='dossier-index'),
    path('dossierMedicals/<int:id>', views.dossier_detail, name="dossier-detail"), 
    path('dossierMedicals/<int:id>/change/', views.dossier_update, name="dossier-update"),
    path('dossierMedicals/<int:id>/delete/', views.dossier_delete, name="dossier-delete"),
    path('dossierMedicals/add/', views.dossier_create, name="dossier-create"),

    path('rendezVouss/', views.rendez_index, name='rendez-index'),
    path('rendezVouss/<int:id>', views.rendez_detail, name="rendez-detail"), 
    path('rendezVouss/<int:id>/change/', views.rendez_update, name="rendez-update"),
    path('rendezVouss/<int:id>/delete/', views.rendez_delete, name="rendez-delete"),
    path('rendezVouss/add/', views.rendez_create, name="rendez-create"),

    path('disponibilites/', views.disponibilite_index, name='disponibilite-index'),
    path('disponibilites/<int:id>', views.disponibilite_detail, name="disponibilite-detail"), 
    path('disponibilites/<int:id>/change/', views.disponibilite_update, name="disponibilite-update"),
    path('disponibilites/<int:id>/delete/', views.disponibilite_delete, name="disponibilite-delete"),
    path('disponibilites/add/', views.disponibilite_create, name="disponibilite-create"),

    
]
