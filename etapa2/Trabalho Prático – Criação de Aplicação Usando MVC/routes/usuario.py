from flask import Blueprint
from controllers import UsuarioController

usuario_bp = Blueprint("usuario_bp", __name__)
usuario_bp.add_url_route("/usuarios", view_func = busca_usuarios, methods = ["GET"])
