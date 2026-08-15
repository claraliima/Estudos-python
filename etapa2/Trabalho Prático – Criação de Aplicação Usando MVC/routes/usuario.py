from flask import Blueprint
from controllers import UsuarioController

usuario_bp = Blueprint("usuario_bp", __name__)
usuario_bp.add_url_rule("/usuarios", view_func=UsuarioController.listar, methods=["GET"])
usuario_bp.add_url_rule("/usuarios/", view_func=None, methods=["POST"])
usuario_bp.add_url_rule("/usuarios", view_func=None, methods=["PUT"])
usuario_bp.add_url_rule("/usuarios/", view_func=UsuarioController.excluir, methods=["DELETE"])
usuario_bp.add_url_rule("/usuarios/Chamados", view_func=UsuarioController.chamados_usuario, methods=["GET"])
