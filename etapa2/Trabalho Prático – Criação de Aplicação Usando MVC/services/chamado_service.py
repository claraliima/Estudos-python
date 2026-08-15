from repositories import ChamadoRepository
from database import db

class ChamadoService:
    @staticmethod
    def verificar_vinculacao(usuario_id):
        if not usuario_id:
            raise ValueError("Chamado deve estar vinculado a um usuário.")
        return True
    @staticmethod
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
    @staticmethod
    def verificar_usuario(id):
        if ChamadoRepository.buscar_por_id(id):
            return 200
        else: 
            return 404
        
    @staticmethod
    def listar_chamados_abertos(id):
        return ChamadoRepository.listar_chamados_abertos(id)
    
    @staticmethod
    def listar_chamados_prioridade():
        return ChamadoRepository.listar_prioridade_alta()
    
    @staticmethod
    def deletar_chamado(id):
        if id == ChamadoRepository.buscar_por_id(id):
            ChamadoRepository.deletar(id)
            return 200
        return 404
