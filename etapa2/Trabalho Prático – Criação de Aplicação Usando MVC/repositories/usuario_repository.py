from models import Usuario, Chamado
from database import db

class UsuarioRepository:

    @staticmethod
    def buscar_por_id(id):
        return Usuario.query.get(id)
    
    @staticmethod
    def listar_todos():
        return Usuario.query.order_by(Usuario.id.asc()).all()
    
    @staticmethod
    def criar(Usuario):
        db.session.add(Usuario)
        db.session.commit()

    @staticmethod
    def deletar(Usuario):
        db.session.delete(Usuario)
        db.session.commit()

    @staticmethod
    def atualizar(id, nome, email, setor):
        usuario = Usuario.query.get(id)
        if usuario:
            usuario.nome = nome
            usuario.email = email
            usuario.setor = setor
            db.session.commit()

    @staticmethod
    def listar_chamados_usuario(id):
        return Chamado.query.filter(
            Chamado.usuario_id == id,
            Chamado.prioridade == "Alta",
            Chamado.status != "Encerrado"
        ).all()
            