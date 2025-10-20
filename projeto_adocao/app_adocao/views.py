from django.shortcuts import get_object_or_404, render, redirect
from .models import Animal
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import SignUpForm




def index(request):
    return render(request,'site/index.html')


def adotar(request):
    especie = request.GET.get('especie')
    
    if especie in ['gato', 'cao']:
        animais = Animal.objects.filter(especie=especie)
    else:
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
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta criada com sucesso! Agora pode entrar.')
            return redirect('sign_in')
        else:
            messages.error(request, 'Por favor, corrija os erros no formulário.')
    else:
        form = SignUpForm()

    return render(request, 'site/sign_up.html', {'form': form})





def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'site/sign_in.html', {'error': 'Erro na palavra passe ou nome de utilizador.'})
    return render(request, 'site/sign_in.html')

from django.contrib.auth import logout

from django.contrib.auth import logout

def sign_out(request):
    logout(request)
    return redirect('index')
