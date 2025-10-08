from django.shortcuts import get_object_or_404, render, redirect
from .models import Animal
from django.contrib.auth import login


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


