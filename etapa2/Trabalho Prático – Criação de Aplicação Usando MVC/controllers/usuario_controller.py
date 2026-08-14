from services import UsuarioService
from flask import jsonify, request

def validar_campos_obrigatorios(UsuarioController):
    if request.method == "POST":
        if not UsuarioController.nome:
            return jsonify({
                "O campo nome deve ser preenchido" 
            })
        if not UsuarioController.email:
            return jsonify({
                "O campo email deve ser preenchido" 
            })
        
class UsuarioController:
    pass