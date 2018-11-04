from django.shortcuts import render

def index(request):
    return render(request,'pages/index.html')

def curso1(request):
    return render(request,'pages/curso1.html')

def curso2(request):
    return render(request,'pages/curso2.html')

def cadastro(request):
    return render(request,'pages/cadastro.html')
    
def vestibular(request):
    return render(request,'pages/vestibular.html')

def login(request):
    return render(request,'pages/login.html')
