from django.db import models
from datetime import date

class Usuario(models.Model):
    nome = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    celular = models.TextField(max_length=20)
    dt_expiracao = models.DateField(default=date(year=1900, month=1, day=1))
    login = models.TextField(max_length=20, unique=True)
    senha = models.TextField(max_length=20)

    def __str__(self):
        return self.nome

class Coordenador(Usuario):
    pass

class Aluno(Usuario):
    ra = models.IntegerField()
    foto = models.TextField(max_length=255)

    def __str__(self):
        return self.nome

class Professor(Usuario):
    apelido = models.TextField(max_length=255)

    def __str__(self):
        return self.apelido