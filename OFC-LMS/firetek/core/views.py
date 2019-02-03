from django.http import HttpResponseRedirect
from django.shortcuts import render
from core.models import Usuario, Aluno, Professor, Coordenador

def index(request):
    return render(request,'pages/index.html')

def curso1(request):
    return render(request,'pages/curso1.html')

def curso2(request):
    return render(request,'pages/curso2.html')

def cadastro(request):
    return render(request,'pages/cadastro.html')
    
def usr(request):
    return render(request,'pages/usr.html')

def table(request):
    #Armazena na variavel aluno todos os objetos da tabela de Alunos
    aluno = Aluno.objects.all()

    #Armazena na variavel template_name o template (table.html)
    template_name = 'pages/table.html'

    #Esse não entendi muito bem, é o dicionario que vai ser passado como paramentro da 
    #função render abaixo
    context = {
        'aluno': aluno
    }
    return render(request,'pages/table.html', context)

def calendario(request):
    return render(request,'pages/calendario.html')

def login(request):
    return render(request,'pages/login.html')

def contatoProfessores(request):

    #Armazena na variavel aluno todos os objetos da tabela de Professor
    usuario = Professor.objects.all()

    #Armazena na variavel template_name o template (table.html)
    template_name = 'pages/contatoProfessores.html' 
  
    #retorna a função render que recebe o request um template e um dicionario opcional
    #  #Armazena na variavel template_name o template (table.html)    
    context = {
        'usuario': usuario
    }
    return render(request,'pages/contatoProfessores.html', context)



def professor(request):
    return render(request, 'pages/Professor.html')