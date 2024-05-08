from django.shortcuts import render,HttpResponse,redirect, get_object_or_404
from .models import Utilisateur
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login

# Create your views here.



def HomePage(request):
    return render (request, 'home.html')



def registrationPage(request):
    if request.method=='POST':
        name=request.POST.get('nom')
        pseudo=request.POST.get('pseudo')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('password')

        if pass1!=pass2:
            return HttpResponse("ERREUR")
        
        if not pass1:
            return HttpResponse("Le mot de passe ne peut pas être vide.")
        
        nouvel_utilisateur = Utilisateur(nom=name, pseudo=pseudo, email=email, password=pass2)
        nouvel_utilisateur.save()


        return redirect('login')


    return render (request, 'registration.html')


def registration(request):
    return render (request, 'registration.html')



def LoginPage(request):
    error_message = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'admin' and password == '2023':
            return redirect('adminis')
        else:
            return redirect('userspace')
        
    return render(request, 'login.html')




def AdminisPage(request):

    utilisateurs = Utilisateur.objects.all()  # Récupérez tous les utilisateurs

    context = {
        'utilisateurs': utilisateurs,  # Passez les utilisateurs au contexte
    }

    if request.method=='POST':
        name=request.POST.get('nom')
        pseudo=request.POST.get('pseudo')
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        if not name:
            return HttpResponse("Le champ 'nom' ne peut pas être vide.")
        elif not pseudo:
            return HttpResponse("Le pseudo ne peut pas être vide.")
        elif not email:
            return HttpResponse("L'email ne peut pas être vide.")
        elif not password:
            return HttpResponse("Le mot de passe ne peut pas être vide.")
        
        nouvel_utilisateur = Utilisateur(nom=name, pseudo=pseudo, email=email, password=password)
        nouvel_utilisateur.save()

    return render (request, 'adminis.html', context)



def ModifierPage(request, pk):
    utilisateur = get_object_or_404(Utilisateur, pk=pk)

    if request.method == 'POST':
        utilisateur.nom = request.POST.get('nom')
        utilisateur.pseudo = request.POST.get('pseudo')
        utilisateur.email = request.POST.get('email')
        utilisateur.password = request.POST.get('password')
        utilisateur.save()

        return redirect('adminis')

    context = {
        'utilisateur': utilisateur,
    }

    return render(request, 'modifier.html', context)


def SupprimerPage(request, pk):
    utilisateur = get_object_or_404(Utilisateur, pk = pk)

    if request.method == 'POST':
        utilisateur.delete()
        return redirect('adminis')
    

    context={
        "utilisateur": utilisateur,
    }
    
    return render(request, 'supprimer.html', context)


def UserspacePage(request):
    return render (request, 'userspace.html')


def logout(request):
    return redirect('login')