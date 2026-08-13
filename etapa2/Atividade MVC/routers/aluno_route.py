from flask import Blueprint
from controllers.aluno_controller import AlunoController

aluno_bp = Blueprint("aluno", __name__)

aluno_bp.add_url_rule("/", view_func = AlunoController.index, methods=["GET"])
aluno_bp.add_url_rule("/alunos", view_func = AlunoController.listar, methods=["GET"])
aluno_bp.add_url_rule("/alunos", view_func = AlunoController.cadastrar, methods=["POST"])
aluno_bp.add_url_rule("/alunos/<int:id>", view_func = AlunoController.buscar, methods=["GET"])
aluno_bp.add_url_rule("/alunos/<int:id>", view_func = AlunoController.atualizar, methods=["PUT"])
aluno_bp.add_url_rule("/alunos/<int:id>", view_func = AlunoController.excluir, methods=["DELETE"])
aluno_bp.add_url_rule("/alunos/<int:id>/ativar", view_func = AlunoController.ativar, methods=["PATCH"])
aluno_bp.add_url_rule("/alunos/<int:id>/C", view_func = AlunoController.desativar, methods=["PATCH"])
aluno_bp.add_url_rule("/estatisticas", view_func = AlunoController.estatisticas, methods=["GET"])
