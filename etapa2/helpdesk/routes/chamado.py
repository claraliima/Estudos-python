from flask import Blueprint
from controllers import ChamadoController

chamado_bp = Blueprint("chamado_bp", __name__)

# Rotas específicas precisam vir antes das rotas com <int:id> para não haver conflito de matching
chamado_bp.add_url_rule("/chamados/abertos", view_func=ChamadoController.listar_abertos, methods=["GET"])
chamado_bp.add_url_rule(
    "/chamados/prioridade/alta", view_func=ChamadoController.listar_prioridade_alta, methods=["GET"]
)
chamado_bp.add_url_rule("/estatisticas", view_func=ChamadoController.estatisticas, methods=["GET"])

chamado_bp.add_url_rule("/chamados", view_func=ChamadoController.listar, methods=["GET"])
chamado_bp.add_url_rule("/chamados/<int:id>", view_func=ChamadoController.buscar, methods=["GET"])
chamado_bp.add_url_rule("/chamados", view_func=ChamadoController.criar, methods=["POST"])
chamado_bp.add_url_rule("/chamados/<int:id>", view_func=ChamadoController.atualizar, methods=["PUT"])
chamado_bp.add_url_rule("/chamados/<int:id>", view_func=ChamadoController.deletar, methods=["DELETE"])

chamado_bp.add_url_rule("/chamados/<int:id>/iniciar", view_func=ChamadoController.iniciar, methods=["PATCH"])
chamado_bp.add_url_rule("/chamados/<int:id>/encerrar", view_func=ChamadoController.encerrar, methods=["PATCH"])
