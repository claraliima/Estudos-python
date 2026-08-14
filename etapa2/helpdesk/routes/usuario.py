from flask import Blueprint
from controllers import UsuarioController

usuario_bp = Blueprint("usuario_bp", __name__)

usuario_bp.add_url_rule("/usuarios", view_func=UsuarioController.listar, methods=["GET"])
usuario_bp.add_url_rule("/usuarios/<int:id>", view_func=UsuarioController.buscar, methods=["GET"])
usuario_bp.add_url_rule("/usuarios", view_func=UsuarioController.criar, methods=["POST"])
usuario_bp.add_url_rule("/usuarios/<int:id>", view_func=UsuarioController.atualizar, methods=["PUT"])
usuario_bp.add_url_rule("/usuarios/<int:id>", view_func=UsuarioController.deletar, methods=["DELETE"])
usuario_bp.add_url_rule(
    "/usuarios/<int:id>/chamados", view_func=UsuarioController.listar_chamados, methods=["GET"]
)
