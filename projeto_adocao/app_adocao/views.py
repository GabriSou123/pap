from django.shortcuts import get_object_or_404, render, redirect
from .models import Animal
from .models import PerfilUtilizador
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse


@login_required
def index(request):
    return render(request, 'site/index.html')


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
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'As palavras passe não coincidem!')
            return redirect('sign_up')

        if PerfilUtilizador.objects.filter(username=username).exists():
            messages.error(request, 'O username já está em uso!')
            return redirect('sign_up')

        if PerfilUtilizador.objects.filter(email=email).exists():
            messages.error(request, 'O e-mail já está em uso!')
            return redirect('sign_up')

        user = PerfilUtilizador.objects.create_user(username=username, email=email, password=password)
        user.save()

        login(request, user)
        messages.success(request, 'Conta criada com sucesso!')
        return redirect('index')

    return render(request, 'site/sign_up.html')


def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Bem-vindo(a) de volta!')
            return redirect('index')
        else:
            messages.error(request, 'Nome de usuário ou senha inválidos!')
            return redirect('sign_in')

    return render(request, 'site/sign_in.html')
