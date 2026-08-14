from repositories import UsuarioRepository
from models import Usuario


class UsuarioService:

    @staticmethod
    def listar_usuarios():
        return UsuarioRepository.listar_todos()

    @staticmethod
    def buscar_usuario(id):
        usuario = UsuarioRepository.buscar_por_id(id)
        if not usuario:
            raise ValueError("Usuário não encontrado.")
        return usuario

    @staticmethod
    def criar_usuario(nome, email, setor):
        if not nome:
            raise ValueError("Nome é obrigatório.")
        if not email:
            raise ValueError("E-mail é obrigatório.")
        if UsuarioRepository.buscar_por_email(email):
            raise ValueError("Já existe um usuário cadastrado com este e-mail.")

        usuario = Usuario(nome=nome, email=email, setor=setor)
        return UsuarioRepository.criar(usuario)

    @staticmethod
    def atualizar_usuario(id, nome=None, email=None, setor=None):
        usuario = UsuarioService.buscar_usuario(id)

        if nome is not None and not nome:
            raise ValueError("Nome é obrigatório.")
        if email is not None:
            if not email:
                raise ValueError("E-mail é obrigatório.")
            existente = UsuarioRepository.buscar_por_email(email)
            if existente and existente.id != usuario.id:
                raise ValueError("Já existe um usuário cadastrado com este e-mail.")

        return UsuarioRepository.atualizar(usuario, nome=nome, email=email, setor=setor)

    @staticmethod
    def excluir_usuario(id):
        usuario = UsuarioService.buscar_usuario(id)

        if UsuarioRepository.contar_chamados_usuario(id) > 0:
            raise ValueError("Não é possível excluir um usuário que possua chamados cadastrados.")

        return UsuarioRepository.deletar(usuario)

    @staticmethod
    def listar_chamados_do_usuario(id):
        UsuarioService.buscar_usuario(id)
        return UsuarioRepository.listar_chamados_usuario(id)
