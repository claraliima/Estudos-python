from flask import request, jsonify
from services import ChamadoService


class ChamadoController:

    @staticmethod
    def listar():
        chamados = ChamadoService.listar_chamados()
        return jsonify([c.to_dict() for c in chamados]), 200

    @staticmethod
    def buscar(id):
        try:
            chamado = ChamadoService.buscar_chamado(id)
            return jsonify(chamado.to_dict()), 200
        except ValueError as e:
            return jsonify({"erro": str(e)}), 404

    @staticmethod
    def criar():
        dados = request.get_json(silent=True) or {}
        try:
            chamado = ChamadoService.criar_chamado(
                titulo=dados.get("titulo"),
                descricao=dados.get("descricao"),
                prioridade=dados.get("prioridade"),
                usuario_id=dados.get("usuario_id"),
                tecnico=dados.get("tecnico")
            )
            return jsonify(chamado.to_dict()), 201
        except ValueError as e:
            return jsonify({"erro": str(e)}), 400

    @staticmethod
    def atualizar(id):
        dados = request.get_json(silent=True) or {}
        try:
            chamado = ChamadoService.atualizar_chamado(
                id,
                titulo=dados.get("titulo"),
                descricao=dados.get("descricao"),
                prioridade=dados.get("prioridade"),
                tecnico=dados.get("tecnico")
            )
            return jsonify(chamado.to_dict()), 200
        except ValueError as e:
            status = 404 if "não encontrado" in str(e) else 400
            return jsonify({"erro": str(e)}), status

    @staticmethod
    def deletar(id):
        try:
            ChamadoService.excluir_chamado(id)
            return jsonify({"mensagem": "Chamado excluído com sucesso."}), 200
        except ValueError as e:
            status = 404 if "não encontrado" in str(e) else 400
            return jsonify({"erro": str(e)}), status

    @staticmethod
    def iniciar(id):
        try:
            chamado = ChamadoService.iniciar_atendimento(id)
            return jsonify(chamado.to_dict()), 200
        except ValueError as e:
            status = 404 if "não encontrado" in str(e) else 400
            return jsonify({"erro": str(e)}), status

    @staticmethod
    def encerrar(id):
        try:
            chamado = ChamadoService.encerrar_chamado(id)
            return jsonify(chamado.to_dict()), 200
        except ValueError as e:
            status = 404 if "não encontrado" in str(e) else 400
            return jsonify({"erro": str(e)}), status

    @staticmethod
    def listar_abertos():
        chamados = ChamadoService.listar_abertos()
        return jsonify([c.to_dict() for c in chamados]), 200

    @staticmethod
    def listar_prioridade_alta():
        chamados = ChamadoService.listar_prioridade_alta()
        return jsonify([c.to_dict() for c in chamados]), 200

    @staticmethod
    def estatisticas():
        return jsonify(ChamadoService.obter_estatisticas()), 200
