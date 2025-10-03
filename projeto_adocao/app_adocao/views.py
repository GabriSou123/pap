from django.shortcuts import get_object_or_404, render, redirect
from .models import Animal

def index(request):
    return render(request,'site/index.html')

def adotar(request):
    animais = Animal.objects.all()
    return render(request, 'site/adotar.html', {'animais': animais})

def contactos(request):
    return render(request,'site/contactos.html')

def sobreNos(request):
    return render(request,'site/sobreNos.html')

def cao1(request):
    return render(request,'animais/cao/cao1.html')

def cao2(request):
    return render(request,'animais/cao/cao2.html')

def gato4(request):
    return render(request,'animais/gato/gato4.html')

def animaisadc(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    return render(request, 'animais/animaisadc.html', {'animal': animal})
