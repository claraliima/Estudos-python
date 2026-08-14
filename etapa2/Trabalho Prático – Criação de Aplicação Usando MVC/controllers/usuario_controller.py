from services import UsuarioService

class UsuarioController:
    
    @staticmethod
    def validar_campos_obrigatorios(UsuarioController):
        if not UsuarioController.nome:
            raise ValueError("Nome é obrigatório.")
        if not UsuarioController.email:
            raise ValueError("E-mail é obrigatório.")