from django.contrib import admin

from .models import *

admin.site.register(Aluno)
admin.site.register(Coordenador)
admin.site.register(Professor)
admin.site.register(Usuario)
admin.site.register(Disciplina)
admin.site.register(DisciplinaOfertada)
admin.site.register(Curso)
admin.site.register(SolicitacaoMatricula)
admin.site.register(Atividade)
admin.site.register(AtividadeVinculada)
admin.site.register(EntregaAtividade)
admin.site.register(Mensagem)

