from django.shortcuts import render
from cabinet.models import Utilisateur, Patient, Disponibilite, RendezVous, DossierMedical
from django.shortcuts import render, redirect
from cabinet.form import PatientForm, UtilisateurForm, DisponibiliteForm, RendezVousForm, DossierMedicalForm
import datetime
from django.http import HttpResponse

# Create your views here.

# Accueil pour visiteur et patient

def accueil_index(request):
    current_nom  = ""
    current_prenom = ""
    current_role = ""
    current_id = ""
    if 'nom' in request.session:
        current_nom = request.session['nom']
    if 'prenom' in request.session:
        current_prenom = request.session['prenom']
    if 'role' in request.session:
        current_role = request.session['role']
    if 'id' in request.session:
        current_id = request.session['id']
    param = {
        'current_nom': current_nom,
        'current_prenom': current_prenom,
        'current_role': current_role,
        'current_id': current_id,
        }
    return render(request, 'accueil/accueil_index.html', param)
    # else:
    #     return redirect('login')
    # return render(request, 'login/login.html')

# Accueil pour utilisateur 

def accueill_index(request):
    current_nom  = ""
    current_prenom = ""
    current_role = ""
    current_id = ""
    if 'nom' in request.session:
        current_nom = request.session['nom']
    if 'prenom' in request.session:
        current_prenom = request.session['prenom']
    if 'role' in request.session:
        current_role = request.session['role']
    if 'id' in request.session:
        current_id = request.session['id']
    rendezsj = RendezVous.objects.all()
    param = {
        'current_nom': current_nom,
        'current_prenom': current_prenom,
        'current_role': current_role,
        'rendezsj':rendezsj,
        'current_id': current_id,
        }
    return render(request, 'accueill/accueill_index.html', param)
    ##
    # today = datetime.datetime.now()
    # print(today)
    # rendezsj = RendezVous.objects.all()
    # rendezss = RendezVous.objects.filter()
    # return render(request, 'accueill/accueill_index.html', {'rendezsj':rendezsj})

# Contact

def contact_index(request):
    current_nom  = ""
    current_prenom = ""
    current_role = ""
    current_id = ""
    if 'nom' in request.session:
        current_nom = request.session['nom']
    if 'prenom' in request.session:
        current_prenom = request.session['prenom']
    if 'role' in request.session:
        current_role = request.session['role']
    if 'id' in request.session:
        current_id = request.session['id']
    param = {
        'current_nom': current_nom,
        'current_prenom': current_prenom,
        'current_role': current_role,
        'current_id': current_id,
        }
    return render(request, 'contact/contact_index.html', param)

# Connexion

# def login(request):
#     if request.method == "POST":
#         email = request.POST.get("email")
#         motDePasse = request.POST.get("motDePasse")
#         userFound = Utilisateur.objects.filter(email=email, motDePasse=motDePasse).values()
#         if userFound:
#             # print("hhhhhhhhhhhhhhhhhhhhh")
#             # print(userFound.nom)
#             user = Utilisateur.objects.get(email=email)
#             print(user.nom)
#             request.session['nom'] = userFound
#             return redirect('accueil-index')
#         else:
#             return HttpResponse('Veuillez vérifier votre email et mot de passe')

#     return render(request, 'login/login.html')

# Pour utilisateur 
def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        motDePasse = request.POST.get("motDePasse")
        userFound = Utilisateur.objects.filter(email=email, motDePasse=motDePasse).values()
        users = Utilisateur.objects.all()
        if userFound:
            for x in users:
                if x.email == email:
                    request.session['nom'] = x.nom
                    request.session['prenom'] = x.prenom
                    request.session['role'] = x.role
            # user = Utilisateur.objects.get(email = email)
            request.session['email'] = email
            # request.session['user'] = userFound
            return redirect('accueill-index')
        else:
            patientFound = Patient.objects.filter(email=email, motDePasse=motDePasse).values()
            patients = Patient.objects.all()
            if patientFound:
                for x in patients:
                    if x.email == email:
                        request.session['nom'] = x.nom
                        request.session['prenom'] = x.prenom
                        request.session['id'] = x.id
                        # request.session['prenom'] = null
                # user = Utilisateur.objects.get(email = email)
                request.session['email'] = email
                # request.session['user'] = userFound
                return redirect('accueil-index')
            else:
                return HttpResponse('Veuillez vérifier votre email et mot de passe')
    current_nom  = ""
    current_prenom = ""
    current_role = ""
    current_id = ""
    if 'nom' in request.session:
        current_nom = request.session['nom']
    if 'prenom' in request.session:
        current_prenom = request.session['prenom']
    if 'role' in request.session:
        current_role = request.session['role']
    if 'id' in request.session:
        current_id = request.session['id']
    param = {
        'current_nom': current_nom,
        'current_prenom': current_prenom,
        'current_role': current_role,
        'current_id': current_id,
        }
    return render(request, 'login/login.html', param)

#Logout
def logout(request):
    try:
        del request.session['nom']
        del request.session['prenom']
        del request.session['role']
    except:
        return redirect('login')

    return redirect('login')

# Inscription patient

def register(request):
    if request.method == "POST":
        nom = request.POST.get("nom")
        prenom = request.POST.get("prenom")
        cin = request.POST.get("cin")
        dateNaissance = request.POST.get("dateNaissance")
        numeroTelephone = request.POST.get("numeroTelephone")
        sexe = request.POST.get("sexe")
        adresse = request.POST.get("adresse")
        profession = request.POST.get("profession")
        email = request.POST.get("email")
        motDePasse = request.POST.get("motDePasse")
    current_nom  = ""
    current_prenom = ""
    current_role = ""
    current_id = ""
    if 'nom' in request.session:
        current_nom = request.session['nom']
    if 'prenom' in request.session:
        current_prenom = request.session['prenom']
    if 'role' in request.session:
        current_role = request.session['role']
    if 'id' in request.session:
        current_id = request.session['id']
    param = {
        'current_nom': current_nom,
        'current_prenom': current_prenom,
        'current_role': current_role,
        'current_id': current_id,
        }
    return render(request, 'register/register.html', param)

# Inscription dossier 

def registerr(request):
    if request.method == "POST":
        dateCreation = request.POST.get("dateCreation")
        groupeSanguin = request.POST.get("groupeSanguin")
        taille = request.POST.get("taille")
        poids = request.POST.get("poids")
        assuranceMaladie = request.POST.get("assuranceMaladie")
        allergies = request.POST.get("allergies")
        vaccination = request.POST.get("vaccination")
        # patient = request.POST.get("patient")
    current_nom  = ""
    current_prenom = ""
    current_role = ""
    current_id = ""
    if 'nom' in request.session:
        current_nom = request.session['nom']
    if 'prenom' in request.session:
        current_prenom = request.session['prenom']
    if 'role' in request.session:
        current_role = request.session['role']
    if 'id' in request.session:
        current_id = request.session['id']
    param = {
        'current_nom': current_nom,
        'current_prenom': current_prenom,
        'current_role': current_role,
        'current_id': current_id,
        }
    return render(request, 'registerr/registerr.html', param)

# Statistique 

def statistique(request):
    current_nom  = ""
    current_prenom = ""
    current_role = ""
    current_id = ""
    if 'nom' in request.session:
        current_nom = request.session['nom']
    if 'prenom' in request.session:
        current_prenom = request.session['prenom']
    if 'role' in request.session:
        current_role = request.session['role']
    if 'id' in request.session:
        current_id = request.session['id']
    param = {
        'current_nom': current_nom,
        'current_prenom': current_prenom,
        'current_role': current_role,
        'current_id': current_id,
        }
    return render(request, 'statistique/statistique.html', param)

# Facture 

def facture(request):
    patients = Patient.objects.all()
    rendezs = RendezVous.objects.all()
    # count = []
    # for p in patients:
    #     v = 0
    #     for r in rendezs:
    #         if r.patient == p.id:
    #             v += 1
    #     count.append(v)

    # print('count')
    # print(count)
    current_nom  = ""
    current_prenom = ""
    current_role = ""
    current_id = ""
    if 'nom' in request.session:
        current_nom = request.session['nom']
    if 'prenom' in request.session:
        current_prenom = request.session['prenom']
    if 'role' in request.session:
        current_role = request.session['role']
    if 'id' in request.session:
        current_id = request.session['id']
    param = {
        'current_nom': current_nom,
        'current_prenom': current_prenom,
        'current_role': current_role,
        'patients':patients,
        'rendezs':rendezs,
        'current_id': current_id,
        }
    return render(request, 'facture/facture.html',param)

# Patient

def patient_index(request):
    patients = Patient.objects.all()
    current_nom  = ""
    current_prenom = ""
    current_role = ""
    current_id = ""
    if 'nom' in request.session:
        current_nom = request.session['nom']
    if 'prenom' in request.session:
        current_prenom = request.session['prenom']
    if 'role' in request.session:
        current_role = request.session['role']
    if 'id' in request.session:
        current_id = request.session['id']
    param = {
        'current_nom': current_nom,
        'current_prenom': current_prenom,
        'current_role': current_role,
        'patients':patients,
        'current_id': current_id,
        }
    return render(request, 'patient/patient_index.html',param)

def patient_detail(request, id):

    patient = Patient.objects.get(id=id)
    dossier = DossierMedical.objects.get(patient=id)
    rendezs = RendezVous.objects.filter(patient=id)
    # rendez = RendezVous.objects.get(patient=id)
    current_nom  = ""
    current_prenom = ""
    current_role = ""
    current_id = ""
    if 'nom' in request.session:
        current_nom = request.session['nom']
    if 'prenom' in request.session:
        current_prenom = request.session['prenom']
    if 'role' in request.session:
        current_role = request.session['role']
    if 'id' in request.session:
        current_id = request.session['id']
    param = {
        'current_nom': current_nom,
        'current_prenom': current_prenom,
        'current_role': current_role,
        'patient':patient,
        'dossier':dossier,
        'rendezs':rendezs,
        'current_id': current_id,
        }
    return render(request, 'info/patient_info.html',param)

def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save()
            return redirect('patient-detail', patient.id)
    else:
        form = PatientForm()
    current_nom  = ""
    current_prenom = ""
    current_role = ""
    current_id = ""
    if 'nom' in request.session:
        current_nom = request.session['nom']
    if 'prenom' in request.session:
        current_prenom = request.session['prenom']
    if 'role' in request.session:
        current_role = request.session['role']
    if 'id' in request.session:
        current_id = request.session['id']
    param = {
        'current_nom': current_nom,
        'current_prenom': current_prenom,
        'current_role': current_role,
        'form': form,
        'current_id': current_id,
        }
    return render(request,'patient/patient_create.html',param)

def patient_update(request, id):
    patient = Patient.objects.get(id=id)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient-detail', patient.id)
    else:
        form = PatientForm(instance=patient)
    current_nom  = ""
    current_prenom = ""
    current_role = ""
    current_id = ""
    if 'nom' in request.session:
        current_nom = request.session['nom']
    if 'prenom' in request.session:
        current_prenom = request.session['prenom']
    if 'role' in request.session:
        current_role = request.session['role']
    if 'id' in request.session:
        current_id = request.session['id']
    param = {
        'current_nom': current_nom,
        'current_prenom': current_prenom,
        'current_role': current_role,
        'form': form,
        'current_id': current_id,
        }
    return render(request,'patient/patient_update.html',param)

def patient_delete(request, id):
    patient = Patient.objects.get(id=id)
    if request.method == 'POST':
        patient.delete()
        return redirect('patient-index')
    current_nom  = ""
    current_prenom = ""
    current_role = ""
    current_id = ""
    if 'nom' in request.session:
        current_nom = request.session['nom']
    if 'prenom' in request.session:
        current_prenom = request.session['prenom']
    if 'role' in request.session:
        current_role = request.session['role']
    if 'id' in request.session:
        current_id = request.session['id']
    param = {
        'current_nom': current_nom,
        'current_prenom': current_prenom,
        'current_role': current_role,
        'patient': patient, 
        'current_id': current_id,
        }
    return render(request,'patient/patient_delete.html',param)

# Utilisateur

def utilisateur_index(request):

    utilisateurs = Utilisateur.objects.all()
    current_nom  = ""
    current_prenom = ""
    current_role = ""
    current_id = ""
    if 'nom' in request.session:
        current_nom = request.session['nom']
    if 'prenom' in request.session:
        current_prenom = request.session['prenom']
    if 'role' in request.session:
        current_role = request.session['role']
    if 'id' in request.session:
        current_id = request.session['id']
    param = {
        'current_nom': current_nom,
        'current_prenom': current_prenom,
        'current_role': current_role,
        'utilisateurs':utilisateurs,
        'current_id': current_id,
        }
    return render(request, 'utilisateur/utilisateur_index.html',param)

def utilisateur_detail(request, id):

    utilisateurs = Utilisateur.objects.get(id=id)
    current_nom  = ""
    current_prenom = ""
    current_role = ""
    current_id = ""
    if 'nom' in request.session:
        current_nom = request.session['nom']
    if 'prenom' in request.session:
        current_prenom = request.session['prenom']
    if 'role' in request.session:
        current_role = request.session['role']
    if 'id' in request.session:
        current_id = request.session['id']
    param = {
        'current_nom': current_nom,
        'current_prenom': current_prenom,
        'current_role': current_role,
        'utilisateurs':utilisateurs,
        'current_id': current_id,
        }
    return render(request, 'utilisateur/utilisateur_detail.html',param)

def utilisateur_create(request):
    if request.method == 'POST':
        form = UtilisateurForm(request.POST)
        if form.is_valid():
            utilisateur = form.save()
            return redirect('utilisateur-detail', utilisateur.id)
    else:
        form = UtilisateurForm()
    current_nom  = ""
    current_prenom = ""
    current_role = ""
    current_id = ""
    if 'nom' in request.session:
        current_nom = request.session['nom']
    if 'prenom' in request.session:
        current_prenom = request.session['prenom']
    if 'role' in request.session:
        current_role = request.session['role']
    if 'id' in request.session:
        current_id = request.session['id']
    param = {
        'current_nom': current_nom,
        'current_prenom': current_prenom,
        'current_role': current_role,
        'form': form,
        'current_id': current_id,
        }
    return render(request,'utilisateur/utilisateur_create.html',param)

def utilisateur_update(request, id):
    utilisateur = Utilisateur.objects.get(id=id)
    if request.method == 'POST':
        form = UtilisateurForm(request.POST, instance=utilisateur)
        if form.is_valid():
            form.save()
            return redirect('utilisateur-detail', utilisateur.id)
    else:
        form = UtilisateurForm(instance=utilisateur)
    current_nom  = ""
    current_prenom = ""
    current_role = ""
    current_id = ""
    if 'nom' in request.session:
        current_nom = request.session['nom']
    if 'prenom' in request.session:
        current_prenom = request.session['prenom']
    if 'role' in request.session:
        current_role = request.session['role']
    if 'id' in request.session:
        current_id = request.session['id']
    param = {
        'current_nom': current_nom,
        'current_prenom': current_prenom,
        'current_role': current_role,
        'form': form,
        'current_id': current_id,
        }
    return render(request,'utilisateur/utilisateur_update.html',param)

def utilisateur_delete(request, id):
    utilisateur = Utilisateur.objects.get(id=id)
    if request.method == 'POST':
        utilisateur.delete()
        return redirect('utilisateur-index')
    current_nom  = ""
    current_prenom = ""
    current_role = ""
    current_id = ""
    if 'nom' in request.session:
        current_nom = request.session['nom']
    if 'prenom' in request.session:
        current_prenom = request.session['prenom']
    if 'role' in request.session:
        current_role = request.session['role']
    if 'id' in request.session:
        current_id = request.session['id']
    param = {
        'current_nom': current_nom,
        'current_prenom': current_prenom,
        'current_role': current_role,
        'utilisateur': utilisateur,
        'current_id': current_id,
        }
    return render(request,'utilisateur/utilisateur_delete.html',param)

# Dossier medical

def dossier_index(request):

    dossiers = DossierMedical.objects.all()
    current_nom  = ""
    current_prenom = ""
    current_role = ""
    current_id = ""
    if 'nom' in request.session:
        current_nom = request.session['nom']
    if 'prenom' in request.session:
        current_prenom = request.session['prenom']
    if 'role' in request.session:
        current_role = request.session['role']
    if 'id' in request.session:
        current_id = request.session['id']
    param = {
        'current_nom': current_nom,
        'current_prenom': current_prenom,
        'current_role': current_role,
        'dossiers':dossiers,
        'current_id': current_id,
        }
    return render(request, 'dossierMedical/dossier_index.html',param)

def dossier_detail(request, id):

    dossiers = DossierMedical.objects.get(id=id)
    current_nom  = ""
    current_prenom = ""
    current_role = ""
    current_id = ""
    if 'nom' in request.session:
        current_nom = request.session['nom']
    if 'prenom' in request.session:
        current_prenom = request.session['prenom']
    if 'role' in request.session:
        current_role = request.session['role']
    if 'id' in request.session:
        current_id = request.session['id']
    param = {
        'current_nom': current_nom,
        'current_prenom': current_prenom,
        'current_role': current_role,
        'dossiers':dossiers,
        'current_id': current_id,
        }
    return render(request, 'dossierMedical/dossier_detail.html',param)

def dossier_create(request):
    if request.method == 'POST':
        form = DossierMedicalForm(request.POST)
        if form.is_valid():
            dossier = form.save()
            return redirect('dossier-detail', dossier.id)
    else:
        form = DossierMedicalForm()
    current_nom  = ""
    current_prenom = ""
    current_role = ""
    current_id = ""
    if 'nom' in request.session:
        current_nom = request.session['nom']
    if 'prenom' in request.session:
        current_prenom = request.session['prenom']
    if 'role' in request.session:
        current_role = request.session['role']
    if 'id' in request.session:
        current_id = request.session['id']
    param = {
        'current_nom': current_nom,
        'current_prenom': current_prenom,
        'current_role': current_role,
        'form': form,
        'current_id': current_id,
        }
    return render(request,'dossierMedical/dossier_create.html',param)

def dossier_update(request, id):
    dossier = DossierMedical.objects.get(id=id)
    if request.method == 'POST':
        form = DossierMedicalForm(request.POST, instance=dossier)
        if form.is_valid():
            form.save()
            return redirect('dossier-detail', dossier.id)
    else:
        form = DossierMedicalForm(instance=dossier)
    current_nom  = ""
    current_prenom = ""
    current_role = ""
    current_id = ""
    if 'nom' in request.session:
        current_nom = request.session['nom']
    if 'prenom' in request.session:
        current_prenom = request.session['prenom']
    if 'role' in request.session:
        current_role = request.session['role']
    if 'id' in request.session:
        current_id = request.session['id']
    param = {
        'current_nom': current_nom,
        'current_prenom': current_prenom,
        'current_role': current_role,
        'form': form,
        'current_id': current_id,
        }
    return render(request,'dossierMedical/dossier_update.html',param)

def dossier_delete(request, id):
    dossier = DossierMedical.objects.get(id=id)
    if request.method == 'POST':
        dossier.delete()
        return redirect('dossier-index')
    current_nom  = ""
    current_prenom = ""
    current_role = ""
    current_id = ""
    if 'nom' in request.session:
        current_nom = request.session['nom']
    if 'prenom' in request.session:
        current_prenom = request.session['prenom']
    if 'role' in request.session:
        current_role = request.session['role']
    if 'id' in request.session:
        current_id = request.session['id']
    param = {
        'current_nom': current_nom,
        'current_prenom': current_prenom,
        'current_role': current_role,
        'dossier': dossier,
        'current_id': current_id,
        }
    return render(request,'dossierMedical/dossier_delete.html',param)

# Rendez-vous

def rendez_index(request):

    rendezs = RendezVous.objects.all()
    current_nom  = ""
    current_prenom = ""
    current_role = ""
    current_id = ""
    if 'nom' in request.session:
        current_nom = request.session['nom']
    if 'prenom' in request.session:
        current_prenom = request.session['prenom']
    if 'role' in request.session:
        current_role = request.session['role']
    if 'id' in request.session:
        current_id = request.session['id']
    param = {
        'current_nom': current_nom,
        'current_prenom': current_prenom,
        'current_role': current_role,
        'rendezs':rendezs,
        'current_id': current_id,
        }
    return render(request, 'rendezVous/rendez_index.html',param)

def rendez_detail(request, id):

    rendezs = RendezVous.objects.get(id=id)
    current_nom  = ""
    current_prenom = ""
    current_role = ""
    current_id = ""
    if 'nom' in request.session:
        current_nom = request.session['nom']
    if 'prenom' in request.session:
        current_prenom = request.session['prenom']
    if 'role' in request.session:
        current_role = request.session['role']
    if 'id' in request.session:
        current_id = request.session['id']
    param = {
        'current_nom': current_nom,
        'current_prenom': current_prenom,
        'current_role': current_role,
        'rendezs':rendezs,
        'current_id': current_id,
        }
    return render(request, 'rendezVous/rendez_detail.html',param)

def rendez_create(request):
    if request.method == 'POST':
        form = RendezVousForm(request.POST)
        if form.is_valid():
            rendez = form.save()
            return redirect('rendez-detail', rendez.id)
    else:
        form = RendezVousForm()

    current_nom  = ""
    current_prenom = ""
    current_role = ""
    current_id = ""
    if 'nom' in request.session:
        current_nom = request.session['nom']
    if 'prenom' in request.session:
        current_prenom = request.session['prenom']
    if 'role' in request.session:
        current_role = request.session['role']
    if 'id' in request.session:
        current_id = request.session['id']
    param = {
        'current_nom': current_nom,
        'current_prenom': current_prenom,
        'current_role': current_role,
        'form': form,
        'current_id': current_id,
        }
    return render(request,'rendezVous/rendez_create.html', param)
    # return render(request,'rendezVous/rendez_create.html',{'form': form})

def rendez_update(request, id):
    rendez = RendezVous.objects.get(id=id)
    if request.method == 'POST':
        form = RendezVousForm(request.POST, instance=rendez)
        if form.is_valid():
            form.save()
            return redirect('rendez-detail', rendez.id)
    else:
        form = RendezVousForm(instance=rendez)
    current_nom  = ""
    current_prenom = ""
    current_role = ""
    current_id = ""
    if 'nom' in request.session:
        current_nom = request.session['nom']
    if 'prenom' in request.session:
        current_prenom = request.session['prenom']
    if 'role' in request.session:
        current_role = request.session['role']
    if 'id' in request.session:
        current_id = request.session['id']
    param = {
        'current_nom': current_nom,
        'current_prenom': current_prenom,
        'current_role': current_role,
        'form': form,
        'current_id': current_id,
        }
    return render(request,'rendezVous/rendez_update.html',param)

def rendez_delete(request, id):
    rendez = RendezVous.objects.get(id=id)
    if request.method == 'POST':
        rendez.delete()
        return redirect('rendez-index')
    current_nom  = ""
    current_prenom = ""
    current_role = ""
    current_id = ""
    if 'nom' in request.session:
        current_nom = request.session['nom']
    if 'prenom' in request.session:
        current_prenom = request.session['prenom']
    if 'role' in request.session:
        current_role = request.session['role']
    if 'id' in request.session:
        current_id = request.session['id']
    param = {
        'current_nom': current_nom,
        'current_prenom': current_prenom,
        'current_role': current_role,
        'rendez': rendez,
        'current_id': current_id,
        }
    return render(request,'rendezVous/rendez_delete.html', param)

# Disponibilite

def disponibilite_index(request):

    disponibilites = Disponibilite.objects.all()
    current_nom  = ""
    current_prenom = ""
    current_role = ""
    current_id = ""
    if 'nom' in request.session:
        current_nom = request.session['nom']
    if 'prenom' in request.session:
        current_prenom = request.session['prenom']
    if 'role' in request.session:
        current_role = request.session['role']
    if 'id' in request.session:
        current_id = request.session['id']
    param = {
        'current_nom': current_nom,
        'current_prenom': current_prenom,
        'current_role': current_role,
        'disponibilites':disponibilites,
        'current_id': current_id,
        }
    return render(request, 'disponibilite/disponibilite_index.html', param)

def disponibilite_detail(request, id):

    disponibilites = Disponibilite.objects.get(id=id)
    current_nom  = ""
    current_prenom = ""
    current_role = ""
    current_id = ""
    if 'nom' in request.session:
        current_nom = request.session['nom']
    if 'prenom' in request.session:
        current_prenom = request.session['prenom']
    if 'role' in request.session:
        current_role = request.session['role']
    if 'id' in request.session:
        current_id = request.session['id']
    param = {
        'current_nom': current_nom,
        'current_prenom': current_prenom,
        'current_role': current_role,
        'disponibilites':disponibilites,
        'current_id': current_id,
        }
    return render(request, 'disponibilite/disponibilite_detail.html',param)

def disponibilite_create(request):
    if request.method == 'POST':
        form = DisponibiliteForm(request.POST)
        if form.is_valid():
            disponibilite = form.save()
            return redirect('disponibilite-detail', disponibilite.id)
    else:
        form = DisponibiliteForm()
    current_nom  = ""
    current_prenom = ""
    current_role = ""
    current_id = ""
    if 'nom' in request.session:
        current_nom = request.session['nom']
    if 'prenom' in request.session:
        current_prenom = request.session['prenom']
    if 'role' in request.session:
        current_role = request.session['role']
    if 'id' in request.session:
        current_id = request.session['id']
    param = {
        'current_nom': current_nom,
        'current_prenom': current_prenom,
        'current_role': current_role,
        'form': form,
        'current_id': current_id,
        }
    return render(request,'disponibilite/disponibilite_create.html',param)

def disponibilite_update(request, id):
    disponibilite = Disponibilite.objects.get(id=id)
    if request.method == 'POST':
        form = DisponibiliteForm(request.POST, instance=disponibilite)
        if form.is_valid():
            form.save()
            return redirect('disponibilite-detail', disponibilite.id)
    else:
        form = DisponibiliteForm(instance=disponibilite)
    current_nom  = ""
    current_prenom = ""
    current_role = ""
    current_id = ""
    if 'nom' in request.session:
        current_nom = request.session['nom']
    if 'prenom' in request.session:
        current_prenom = request.session['prenom']
    if 'role' in request.session:
        current_role = request.session['role']
    if 'id' in request.session:
        current_id = request.session['id']
    param = {
        'current_nom': current_nom,
        'current_prenom': current_prenom,
        'current_role': current_role,
        'form': form,
        'current_id': current_id,
        }
    return render(request,'disponibilite/disponibilite_update.html',param)

def disponibilite_delete(request, id):
    disponibilite = Disponibilite.objects.get(id=id)
    if request.method == 'POST':
        disponibilite.delete()
        return redirect('disponibilite-index')
    current_nom  = ""
    current_prenom = ""
    current_role = ""
    current_id = ""
    if 'nom' in request.session:
        current_nom = request.session['nom']
    if 'prenom' in request.session:
        current_prenom = request.session['prenom']
    if 'role' in request.session:
        current_role = request.session['role']
    if 'id' in request.session:
        current_id = request.session['id']
    param = {
        'current_nom': current_nom,
        'current_prenom': current_prenom,
        'current_role': current_role,
        'disponibilite': disponibilite,
        'current_id': current_id,
        }
    return render(request,'disponibilite/disponibilite_delete.html',param)