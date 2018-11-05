from django.db import models

class Usuario(models.Model):
    login = models.TextField(max_length=20, unique=True)
    senha = models.TextField(max_length=20)

class Aluno(Usuario):
    nome = models.TextField(max_length=255)

    def matriculas(self):
        from .disciplina import SolicitacaoMatricula
        sm = SolicitacaoMatricula.objects.filter(aluno=self)
        return sm