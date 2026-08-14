from flask import request, jsonify
from services import UsuarioService


class UsuarioController:

    @staticmethod
    def listar():
        usuarios = UsuarioService.listar_usuarios()
        return jsonify([u.to_dict() for u in usuarios]), 200

    @staticmethod
    def buscar(id):
        try:
            usuario = UsuarioService.buscar_usuario(id)
            return jsonify(usuario.to_dict()), 200
        except ValueError as e:
            return jsonify({"erro": str(e)}), 404

    @staticmethod
    def criar():
        dados = request.get_json(silent=True) or {}
        try:
            usuario = UsuarioService.criar_usuario(
                nome=dados.get("nome"),
                email=dados.get("email"),
                setor=dados.get("setor")
            )
            return jsonify(usuario.to_dict()), 201
        except ValueError as e:
            return jsonify({"erro": str(e)}), 400

    @staticmethod
    def atualizar(id):
        dados = request.get_json(silent=True) or {}
        try:
            usuario = UsuarioService.atualizar_usuario(
                id,
                nome=dados.get("nome"),
                email=dados.get("email"),
                setor=dados.get("setor")
            )
            return jsonify(usuario.to_dict()), 200
        except ValueError as e:
            status = 404 if "não encontrado" in str(e) else 400
            return jsonify({"erro": str(e)}), status

    @staticmethod
    def deletar(id):
        try:
            UsuarioService.excluir_usuario(id)
            return jsonify({"mensagem": "Usuário excluído com sucesso."}), 200
        except ValueError as e:
            status = 404 if "não encontrado" in str(e) else 400
            return jsonify({"erro": str(e)}), status

    @staticmethod
    def listar_chamados(id):
        try:
            chamados = UsuarioService.listar_chamados_do_usuario(id)
            return jsonify([c.to_dict() for c in chamados]), 200
        except ValueError as e:
            return jsonify({"erro": str(e)}), 404
