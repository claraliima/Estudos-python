from flask import Blueprint
from controllers import ChamadoController

chamado_bp = Blueprint("usuario_bp", __name__)
chamado_bp.add_url_route("/usuarios", view_func = busca_usuarios(), methods = ["GET"])
