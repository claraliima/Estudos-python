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
            
    @staticmethod
    def consultar_email(email):
        return UsuarioRepository.pesquisa_email(email)
    
    @staticmethod
    def listar_usuarios():
        return UsuarioRepository.listar_todos()
    
    @staticmethod
    def listar_chamados_usuario(id):
        return UsuarioRepository.listar_chamados_usuario(id)
    

