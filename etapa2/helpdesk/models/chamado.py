from database import db
from datetime import datetime


class Chamado(db.Model):
    __tablename__ = 'chamado'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(150), nullable=False)
    descricao = db.Column(db.String(500), nullable=False)
    status = db.Column(db.String(20), nullable=False, default="Aberto")
    prioridade = db.Column(db.String(20), nullable=False)
    tecnico = db.Column(db.String(100), nullable=True)
    data_abertura = db.Column(db.DateTime, default=datetime.utcnow)

    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "prioridade": self.prioridade,
            "tecnico": self.tecnico,
            "data_abertura": self.data_abertura.isoformat() if self.data_abertura else None,
            "usuario_id": self.usuario_id,
            "status": self.status
        }
