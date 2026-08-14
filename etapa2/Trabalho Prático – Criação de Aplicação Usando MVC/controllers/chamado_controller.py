from services import ChamadoService
from flask import jsonify, request

def validar_campos_obrigatorios(info):
    if not info.titulo:
        return jsonify({
            "O campo nome deve ser preenchido" 
        }), 400
    if len(info.titulo) <= 5:
        return jsonify({
            "O campo nome deve ser preenchido" 
        }), 400
    if len(info.descricao) <= 10:
        return jsonify({
            "O campo nome deve ser preenchido" 
        }), 400
    if info.usuario_id:
        ChamadoService.verificar_usuario(id)
        return 200
    
class ChamadoController:
    @staticmethod
    def cadastrar(info):
        dados = request.get_json()
        if request.method == "POST":
            if dados:
                validar_campos_obrigatorios(dados)
