from repositories import ChamadoRepository
from database import db

class ChamadoService:
    @staticmethod
    def verificar_vinculacao(usuario_id):
        if not usuario_id:
            raise ValueError("Chamado deve estar vinculado a um usuário.")
        return True
    
    def iniciar_atendimento(id):
        ChamadoRepository.altera_status_atendimento(id)