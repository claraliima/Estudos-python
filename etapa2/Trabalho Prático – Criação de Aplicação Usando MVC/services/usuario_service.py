from repositories import UsuarioRepository, ChamadoRepository
from controllers import UsuarioController
from database import db

class UsuarioService:
    @staticmethod
    def verificar_qtde_chamados(id):
        chamados = UsuarioRepository.listar_chamados_usuario(id)

        if len(chamados) >= 5:
            raise ValueError(
                "Usuário não pode ter mais de 5 chamados de alta prioridade não encerrados."
            )

        return ChamadoRepository.criar
    
    @staticmethod
    def permitir_excluir(id):
        if UsuarioRepository.listar_chamados_usuario(id):
            raise ValueError("Usuário não pode ser excluído, existem chamados vinculados a ele.")
        
        else:
            UsuarioRepository.deletar(UsuarioRepository.buscar_por_id(id))
            
    def criar():
        try:
            UsuarioController.validar_campos_obrigatorios(UsuarioController.nome, UsuarioController.email)
        except ValueError as e:
            print(f"Erro de validação: {e}")
