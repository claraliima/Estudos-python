from repositories import ChamadoRepository, UsuarioRepository
from models import Chamado

PRIORIDADES_VALIDAS = ["Baixa", "Média", "Alta"]
LIMITE_CHAMADOS_ALTA_PRIORIDADE_ABERTOS = 5


class ChamadoService:

    @staticmethod
    def listar_chamados():
        return ChamadoRepository.listar_todos()

    @staticmethod
    def buscar_chamado(id):
        chamado = ChamadoRepository.buscar_por_id(id)
        if not chamado:
            raise ValueError("Chamado não encontrado.")
        return chamado

    @staticmethod
    def validar_dados(titulo, descricao, prioridade):
        if not titulo or len(titulo) < 5:
            raise ValueError("Título é obrigatório e deve possuir pelo menos 5 caracteres.")
        if not descricao or len(descricao) < 10:
            raise ValueError("Descrição é obrigatória e deve possuir pelo menos 10 caracteres.")
        if prioridade not in PRIORIDADES_VALIDAS:
            raise ValueError(f"Prioridade deve ser uma das seguintes: {', '.join(PRIORIDADES_VALIDAS)}.")

    @staticmethod
    def criar_chamado(titulo, descricao, prioridade, usuario_id, tecnico=None):
        if not usuario_id or not UsuarioRepository.buscar_por_id(usuario_id):
            raise ValueError("O chamado deve estar vinculado a um usuário existente.")

        ChamadoService.validar_dados(titulo, descricao, prioridade)

        if prioridade == "Alta":
            qtde = ChamadoRepository.contar_prioritarios_nao_encerrados(usuario_id, "Alta")
            if qtde >= LIMITE_CHAMADOS_ALTA_PRIORIDADE_ABERTOS:
                raise ValueError(
                    "Usuário não pode possuir mais de cinco chamados de prioridade "
                    "Alta que ainda não estejam encerrados."
                )

        chamado = Chamado(
            titulo=titulo,
            descricao=descricao,
            prioridade=prioridade,
            tecnico=tecnico,
            usuario_id=usuario_id,
            status="Aberto"
        )
        return ChamadoRepository.criar(chamado)

    @staticmethod
    def atualizar_chamado(id, titulo=None, descricao=None, prioridade=None, tecnico=None):
        chamado = ChamadoService.buscar_chamado(id)

        titulo_validar = titulo if titulo is not None else chamado.titulo
        descricao_validar = descricao if descricao is not None else chamado.descricao
        prioridade_validar = prioridade if prioridade is not None else chamado.prioridade
        ChamadoService.validar_dados(titulo_validar, descricao_validar, prioridade_validar)

        return ChamadoRepository.atualizar(
            chamado, titulo=titulo, descricao=descricao, prioridade=prioridade, tecnico=tecnico
        )

    @staticmethod
    def excluir_chamado(id):
        chamado = ChamadoService.buscar_chamado(id)
        return ChamadoRepository.deletar(chamado)

    @staticmethod
    def iniciar_atendimento(id):
        chamado = ChamadoService.buscar_chamado(id)
        if chamado.status != "Aberto":
            raise ValueError(
                f"Não é possível iniciar atendimento de um chamado com status '{chamado.status}'."
            )
        return ChamadoRepository.alterar_status(chamado, "Em atendimento")

    @staticmethod
    def encerrar_chamado(id):
        chamado = ChamadoService.buscar_chamado(id)
        if chamado.status != "Em atendimento":
            raise ValueError(
                f"Não é possível encerrar um chamado com status '{chamado.status}'."
            )
        return ChamadoRepository.alterar_status(chamado, "Encerrado")

    @staticmethod
    def listar_abertos():
        return ChamadoRepository.listar_chamados_abertos()

    @staticmethod
    def listar_prioridade_alta():
        return ChamadoRepository.listar_prioridade_alta()

    @staticmethod
    def obter_estatisticas():
        return {
            "usuarios": UsuarioRepository.contar_total(),
            "chamados": ChamadoRepository.contar_total(),
            "abertos": ChamadoRepository.contar_por_status("Aberto"),
            "em_atendimento": ChamadoRepository.contar_por_status("Em atendimento"),
            "encerrados": ChamadoRepository.contar_por_status("Encerrado"),
        }
