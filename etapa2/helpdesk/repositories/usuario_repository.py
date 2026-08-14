from models import Usuario, Chamado
from database import db


class UsuarioRepository:

    @staticmethod
    def buscar_por_id(id):
        return Usuario.query.get(id)

    @staticmethod
    def buscar_por_email(email):
        return Usuario.query.filter(Usuario.email == email).first()

    @staticmethod
    def listar_todos():
        return Usuario.query.order_by(Usuario.id.asc()).all()

    @staticmethod
    def criar(usuario):
        db.session.add(usuario)
        db.session.commit()
        return usuario

    @staticmethod
    def deletar(usuario):
        db.session.delete(usuario)
        db.session.commit()
        return True

    @staticmethod
    def atualizar(usuario, nome=None, email=None, setor=None):
        if nome is not None:
            usuario.nome = nome
        if email is not None:
            usuario.email = email
        if setor is not None:
            usuario.setor = setor
        db.session.commit()
        return usuario

    @staticmethod
    def listar_chamados_usuario(id):
        return Chamado.query.filter(Chamado.usuario_id == id).order_by(Chamado.id.asc()).all()

    @staticmethod
    def contar_chamados_usuario(id):
        return Chamado.query.filter(Chamado.usuario_id == id).count()

    @staticmethod
    def contar_total():
        return Usuario.query.count()
