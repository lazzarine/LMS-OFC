class Usuario():
    def __init__(self, id, Login, Senha, Dt_Expiracao):
        self.id = id
        self.Login = Login
        self.Senha = Senha
        self.Dt_Expiracao = Dt_Expiracao


class Coordenador():
    def __init__(self, id , Nome, Email, Celular, Usuario):
        self.id = id
        self.Nome = Nome
        self.Email = Email                       
        self.Celular = Celular
        self.Usuario = Usuario

class Aluno():
    def __init__(self, id, id_Usuario, Nome, Email, Celular, RA, Foto):
        self.id = id
        self.id_Usuario = id_Usuario
        self.Nome = Nome
        self.Email = Email
        self.Celular = Celular
        self.RA = RA
        self.Foto = Foto


class Professor():
    def __init__(self, id, id_Usuario, Email, Celular, Apelido):
        self.id = id
        self.id_Usuario = id_Usuario
        self.Email = Email
        self.Celular = Celular
        self.Apelido = Apelido

class Disciplina():
    def __init__(self, id, Nome, Data, Status, PalnoDeEnsino, 
                CagaHoraria, Competencias, Habilidades, 
                Ementa, ConteudoProgramatico, BibliografiaBasica, BibliografiaComplementar,
                PercentualPratico, PercentualTeorico, idCoordenador):
        self.id = id
        self.Nome = Nome
        self.Data = Data
        self.Status = Status
        self.PlanoDeEnsino = PalnoDeEnsino
        self.CagaHoraria = CagaHoraria
        self.Competencias = Competencias
        self.habilidades = Habilidades
        self.Ementa = Ementa
        self.ConteudoProgramatico = ConteudoProgramatico
        self.BibliografiaBasica = BibliografiaBasica
        self.BibliografiaComplementar = BibliografiaComplementar
        self.PercentualPratico = PercentualPratico
        self.PercentualTeorico = PercentualTeorico
        self.idCoordenador = idCoordenador

class DisciplinaOfertada (self, id, idCoordenador, DtInicioMatricula, DtFimMatricula,
                        idDisciplina, idCurso, ano, semestre, turma, idProfessor,
                        metodologia, recursos, criterioAvaliacao, planoDeAulas):
    self.id = id
    self.idCoordenador = idCoordenador
    self.DtInicioMatricula = DtInicioMatricula
    self.DtFimMatricula = DtFimMatricula
    self.idDisciplina = idDisciplina
    self.idCurso = idCurso
    self.ano = ano 
    self.semestre = semestre
    self.turma = turma
    self.idProfessor = idProfessor
    self.metodologia = metodologia
    self.recursos = recursos
    self.criterioAvaliacao = criterioAvaliacao
    self.planoDeAulas = planoDeAulas

class Curso():
    def __init__(self, id, Nome):
        self.id = id
        self.Nome = Nome
    
    def imprime_curso(self):
        return 'O curso {} possui o id {}'.format(
            self.Nome, self.id
        )

class Solicitacaomatricula():
    def __init__(self, id, idAluno, idDiciplinaOfertada, DtSolicitacao, idCoordenador, Status):
        self.id = id
        self.idAluno = idAluno
        self.idDiciplinaOfertada = idDiciplinaOfertada
        self.DtSolicitacao = DtSolicitacao
        self.idCoordenador = idCoordenador
        self.Status = Status

    def imprime_solicitacaoMatricula(self):
        return 'O aluno {} solicitou no dia {}  a matricula na diciplina {} ofertada pelo {}'.format(
            self.idAluno, self.DtSolicitacao, self.idDiciplinaOfertada, self.idCoordenador, self.Status
        )

class Atividade():
    def __init__(self, id, Titulo, descricao, Conteudo, Tipo, Extras, idProfessor):
        self.id = id
        self.Titulo = Titulo
        self.descricao = descricao
        self.Conteudo = Conteudo
        self.Tipo = Tipo
        self.Extras = Extras
        self.idProfessor = idProfessor

    def imprime_atividade(self):
        

class AtividadeVinculada():
    def __init__(self, id, idAtividade, idProfessor, idDiciplinaOfertada, 
                    Rotulo, Status, DtInicioResposta, DtFimResposta):
        self.id = id
        self.idAtividade = idAtividade
        self.idProfessor = idProfessor
        self.idDiciplinaOfertada = idDiciplinaOfertada
        self.Rotulo = Rotulo
        self.Status = Status
        self.DtInicioResposta = DtInicioResposta
        self.DtFimResposta = DtFimResposta


class Entrega():
    def __init__(self, id, idAluno, idAtividadeVinculada, Titulo, Resposta, 
                    DtEntrega, Status, idProfessor, Nota, DtAvaliacao, Obs):
        self.id = id
        self.idAluno = idAluno
        self.idAtividadeVinculada = idAtividadeVinculada
        self.Titulo = Titulo
        self.Resposta = Resposta
        self.DtEntrega = DtEntrega
        self.Status = Status
        self.idProfessor = idProfessor
        self.Nota = Nota
        self.DtAvaliacao = DtAvaliacao
        self.Obs = Obs

class Mensagem():
    def __init__(self, id, idAluno, idProfessor, Assunto, Referencia, 
                Conteudo, Status, DtEnvio, DtResposta, Resposta):
        self.id = id
        self.idAluno = idAluno
        self.idProfessor = idProfessor
        self.Assunto = Assunto
        self.Referencia = Referencia
        self.Status = Status
        self.DtEnvio = DtEnvio
        self.DtResposta = DtResposta
        self.Resposta = Resposta
