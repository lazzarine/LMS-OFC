from django.shortcuts import render

def index(request):
    return render(request,'pages/index.html')

def curso1(request):
    return render(request,'pages/curso1.html')

def curso2(request):
    return render(request,'pages/curso2.html')

def cadastro(request):
    return render(request,'pages/cadastro.html')
    
def login(request):
    return render(request,'pages/login.html')

def usr(request):
    return render(request,'pages/usr.html')

def table(request):
    return render(request,'pages/table.html')

def calendar(request):
    return render(request,'pages/calendar.html')
