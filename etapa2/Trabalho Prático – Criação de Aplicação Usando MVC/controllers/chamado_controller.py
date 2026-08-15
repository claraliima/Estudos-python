from services import ChamadoService
from flask import jsonify, request
  
class ChamadoController: 
    @staticmethod
    def validar_campos_obrigatorios(dados):
        if not dados.get("titulo"):
            return jsonify({
                "erro": "O campo TITULO deve ser preenchido" 
            }), 400
        if len(dados.get("titulo")) < 5:
            return jsonify({
                "erro": "O campo TITULO deve ser mais que 5 caracteres" 
            }), 400
        if len(dados.get("descricao")) < 10:
            return jsonify({
                "erro": "O campo DESCRICAO deve ser mais que 10 caracteres" 
            }), 400
        if not dados.get("usuario_id"):
            return jsonify({
                "erro": "O chamado deve estar associado a um usuário existente" 
            }), 400
        prioridade = str(dados.get("prioridade")).lower()
        if prioridade:
            if not prioridade == "baixa" or prioridade == "média":
                return jsonify({
                    "erro": "O chamado deve estar associado a um usuário existente" 
                }), 400
            elif not prioridade == "baixa" or prioridade == "alta":
                return jsonify({
                    "erro": "O chamado deve estar associado a um usuário existente" 
                }), 400
            elif not prioridade == "media" or prioridade == "alta":
                return jsonify({
                    "erro": "O chamado deve estar associado a um usuário existente" 
                }), 400
        return True
    
    @staticmethod
    def cria_chamado():
        dados = request.get_json()
        validar_campos_obrigatorios = ChamadoController.validar_campos_obrigatorios(dados)

        if validar_campos_obrigatorios is not True:
            return validar_campos_obrigatorios
    
        chamado = ChamadoService.cria_chamado(
            titulo=dados["titulo"],
            descricao=dados["descricao"],
            status=dados["status"],
            prioridade=dados["prioridade"],
            tecnico=dados["tecnico"],
            data_abertura=dados["data_abertura"]
        )
        return jsonify({
            "mensagem": "Chamado criado",
            "id": chamado.id
        })
            
    @staticmethod
    def atualizar(id):
        dados = request.get_json()
        validar_campos_obrigatorios = ChamadoController.validar_campos_obrigatorios(dados)
        if validar_campos_obrigatorios is not True:
            return validar_campos_obrigatorios

        chamado = ChamadoService.atualiza_chamado(
            titulo=dados["titulo"],
            descricao=dados["descricao"],
            status=dados["status"],
            prioridade=dados["prioridade"],
            tecnico=dados["tecnico"],
            data_abertura=dados["data_abertura"]
        )

        if not chamado:
            return jsonify({"erro": "Chamado não encontrado"}), 404

        return jsonify({
            "mensagem": "Chamado atualizado",
            "id": chamado.id
        })
        
    @staticmethod    
    def chamados_abertos(id):
            return ChamadoService.listar_chamados_abertos(id)
        
    @staticmethod
    def encerrar_chamado(id):
        return ChamadoService.alterar_status(id)
    
    @staticmethod
    def iniciar_atendimento(id):
        return ChamadoService.alterar_status(id)
    
    @staticmethod
    def listar_chamados_prioridade():
        return ChamadoService.listar_chamados_prioridade()
    
    @staticmethod
    def excluir(id):
            ChamadoService.deletar_chamado(id)
            return jsonify({
                ""
            })