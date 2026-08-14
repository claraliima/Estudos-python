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

    def alterar_status(id):
        chamado = ChamadoRepository.buscar_por_id(id)
        if str(chamado.status).lower() == "aberto":
            ChamadoRepository.altera_status_atendimento(chamado.id)
            return 204
        elif str(chamado.status).lower() == "em-andamento":
            ChamadoRepository.altera_status_encerrado(chamado.id)
            return 204
        else:
            return 404

    def verificar_usuario(id):
        if ChamadoRepository.buscar_por_id(id):
            return 200
        else: 
            return 404
