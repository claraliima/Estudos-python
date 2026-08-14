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
    def criar(chamado):
        db.session.add(chamado)
        db.session.commit()
        return chamado

    @staticmethod
    def deletar(chamado):
        db.session.delete(chamado)
        db.session.commit()
        return True

    @staticmethod
    def atualizar(chamado, titulo=None, descricao=None, prioridade=None, tecnico=None):
        if titulo is not None:
            chamado.titulo = titulo
        if descricao is not None:
            chamado.descricao = descricao
        if prioridade is not None:
            chamado.prioridade = prioridade
        if tecnico is not None:
            chamado.tecnico = tecnico
        db.session.commit()
        return chamado

    @staticmethod
    def alterar_status(chamado, novo_status):
        chamado.status = novo_status
        db.session.commit()
        return chamado

    @staticmethod
    def listar_chamados_abertos():
        return Chamado.query.filter(Chamado.status == "Aberto").order_by(Chamado.id.asc()).all()

    @staticmethod
    def listar_prioridade_alta():
        return Chamado.query.filter(Chamado.prioridade == "Alta").order_by(Chamado.id.asc()).all()

    @staticmethod
    def contar_por_status(status):
        return Chamado.query.filter(Chamado.status == status).count()

    @staticmethod
    def contar_total():
        return Chamado.query.count()

    @staticmethod
    def contar_prioritarios_nao_encerrados(usuario_id, prioridade="Alta"):
        return Chamado.query.filter(
            Chamado.usuario_id == usuario_id,
            Chamado.prioridade == prioridade,
            Chamado.status != "Encerrado"
        ).count()
