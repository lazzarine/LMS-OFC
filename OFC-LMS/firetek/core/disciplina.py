from django.db import models
from .usuario import Aluno


class Disciplina(models.Model):
    nome = models.TextField(max_length=255, unique=True)

class Curso(models.Model):
    nome = models.TextField(max_length=255, unique=True)

class DisciplinaOfertada(models.Model):
    ano = models.IntegerField()
    semestre = models.IntegerField()
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)

class SolicitacaoMatricula(models.Model):
    status = models.TextField(max_length=255)
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    disciplina_ofertada = models.ForeignKey(DisciplinaOfertada, on_delete=models.PROTECT)