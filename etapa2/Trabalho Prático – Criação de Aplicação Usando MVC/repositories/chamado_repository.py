from models import Chamado
from database import db

class ChamadoRepository:

    @staticmethod
    def buscar_por_id(id):
        return Chamado.query.get(id)
    
    @staticmethod
    def listar_todos():
        return Chamado.query.order_by(Chamado.id.asc()).all()
    
    @staticmethod
    def criar(Chamado):
        db.session.add(Chamado)
        db.session.commit()
        return Chamado  # Retorna o objeto criado

    @staticmethod
    def deletar(Chamado):
        db.session.delete(Chamado)
        db.session.commit()
        return True  # Retorna uma confirmação de sucesso

    @staticmethod
    def atualizar(id, titulo, descricao, prioridade, tecnico, status):
        chamado = Chamado.query.get(id)
        if chamado:
            chamado.titulo = titulo
            chamado.descricao = descricao
            chamado.prioridade = prioridade
            chamado.tecnico = tecnico
            chamado.status = status
            db.session.commit()
            return chamado  # Retorna o objeto atualizado
        return None  # Retorna None se o chamado não for encontrado

    @staticmethod
    def altera_status_atendimento(id):
        chamado = Chamado.query.get(id)
        if chamado:
            chamado.status = "Em atendimento"
            db.session.commit()
            return chamado  # Retorna o objeto com o status alterado
        return None

    @staticmethod
    def altera_status_encerrado(id):
        chamado = Chamado.query.get(id)
        if chamado:
            chamado.status = "Encerrado"
            db.session.commit()
            return chamado  # Retorna o objeto com o status alterado
        return None

    @staticmethod
    def listar_chamados_abertos():
        return Chamado.query.order_by(Chamado.id.asc()).where(Chamado.status == "Aberto")
    
    @staticmethod
    def listar_prioridade_alta():
        return Chamado.query.order_by(Chamado.id.asc()).where(Chamado.prioridade == "Alta")
    
    @staticmethod
    def contar_prioritarios_nao_encerrados(usuario_id):
        return Chamado.query.filter(
            Chamado.usuario_id == usuario_id,
            Chamado.prioridade == "Alta", 
            Chamado.status != "Encerrado"
        ).count()