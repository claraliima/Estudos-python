from flask import Blueprint
from controllers import ChamadoController

chamado_bp = Blueprint("usuario_bp", __name__)
chamado_bp.add_url_rule("/chamados", view_func=None, methods=["GET"])
chamado_bp.add_url_rule("/chamados/", view_func=ChamadoController.cria_chamado, methods=["POST"])
chamado_bp.add_url_rule("/chamados", view_func=None, methods=["PUT"])
chamado_bp.add_url_rule("/chamados/", view_func=None, methods=["DELETE"])

chamado_bp.add_url_rule("/chamados/<id>/iniciar", view_func=ChamadoController.iniciar_atendimento, methods=["PATCH"])
chamado_bp.add_url_rule("/chamados/<id>/encerrar", view_func=ChamadoController.encerrar_chamado, methods=["PATCH"])
chamado_bp.add_url_rule("/chamados/abertos", view_func=ChamadoController.chamados_abertos, methods=["GET"])
chamado_bp.add_url_rule("/chamados/prioridade/alta", view_func=ChamadoController.listar_chamados_prioridade, methods=["GET"])