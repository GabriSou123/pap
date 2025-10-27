from django.shortcuts import get_object_or_404, render, redirect
from .models import Animal
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required



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



@login_required
def apadrinhar(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)

    if animal.padrinho and animal.padrinho != request.user:
        messages.warning(request, f"O {animal.nome} já foi apadrinhado por outro utilizador.")
        return render(request, 'site/apadrinhar.html', {'animal': animal})

    if request.method == "POST" and "cancelar" in request.POST:
        if animal.padrinho == request.user:
            animal.padrinho = None
            animal.save()
            messages.success(request, f"Apadrinhamento de {animal.nome} cancelado.")
        return render(request, 'site/apadrinhar.html', {'animal': animal})

    if request.method == "POST" and not animal.padrinho:
        animal.padrinho = request.user
        animal.save()
        messages.success(request, f"Parabéns! Agora é o padrinho/madrinha de {animal.nome}.")
        return render(request, 'site/apadrinhar.html', {'animal': animal})

    return render(request, 'site/apadrinhar.html', {'animal': animal})


@login_required
def confirmacao_apadrinhamento(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    return render(request, 'site/confirmacao_apadrinhamento.html', {'animal': animal})



def sign_up(request):
    storage = messages.get_messages(request)
    storage.used = True

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


def sign_out(request):
    logout(request)
    return redirect('index')





    