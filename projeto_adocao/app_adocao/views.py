from django.shortcuts import get_object_or_404, render, redirect
from .models import Animal
from.models import PerfilUtilizador
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User


def index(request):
    return render(request,'site/index.html')

def adotar(request):
    animais = Animal.objects.all()
    return render(request, 'site/adotar.html', {'animais': animais})

def contactos(request):
    return render(request,'site/contactos.html')

def sobreNos(request):
    return render(request,'site/sobreNos.html')


def animaisadc(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    return render(request, 'animais/animaisadc.html', {'animal': animal})


def sign_up(request):
    return render(request,'site/sign_up.html')
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        palavraPasse = request.POST['palavraPasse']
        confirmarPalavraPasse = request.POST['confirmarPalavraPasse']
        if palavraPasse == confirmarPalavraPasse:
            User.objects.create_user(username=username, email=email, palavraPasse=palavraPasse)
            return redirect('sign_in')
        else:
            return render(request, 'sign_up.html', {'error': 'As palavras-passe não coincidem'})
    return render(request, 'sign_up.html')


def sign_in(request):
    return render(request,'site/sign_in.html')
    if request.method == 'POST':
        username = request.POST['username']
        palavraPasse = request.POST['palavraPasse']
        user = authenticate(request, username=username, palavraPasse=palavraPasse)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'sign_in.html', {'error': 'Erro na palavra passe ou nome de utilizador.'})
    return render(request, 'sign_in.html')