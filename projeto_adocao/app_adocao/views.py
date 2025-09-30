from django.shortcuts import render

def index(request):
    return render(request,'site/index.html')

def adotar(request):
    return render(request,'site/adotar.html')

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
