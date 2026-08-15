from services import UsuarioService
from flask import jsonify, request

class UsuarioController:
    @staticmethod
    def validar_campos_obrigatorios(dados):
        if not dados.get("nome"):
            return jsonify({
                "erro": "O campo NOME deve ser preenchido" 
            }), 400
        if not dados.get("email"):
            return jsonify({
                "erro": "O campo EMAIL deve ser preenchido" 
            }), 400
        if dados.get("email") == UsuarioService.consulta_email(dados.get("email")):
            return jsonify({
                "erro": "Esse valor de EMAIL já existe" 
            }), 400
        return True
    
    @staticmethod
    def listar():
        return UsuarioService.listar_usuarios()
    
    @staticmethod
    def chamados_usuario(id):
        return UsuarioService.listar_chamados_usuario(id)
        
    @staticmethod
    def excluir():
        dados  = request.get_json()
        id = dados["id"]
        
        if not id:
            return jsonify({
                "erro": "id é obrigatório"
            }), 400

        try:
            UsuarioService.permitir_excluir(id)
        except ValueError as e:
            return jsonify({
                "erro": str(e)
            }), 400
        