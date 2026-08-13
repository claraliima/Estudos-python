from models.aluno_model import Aluno
from flask import request, jsonify
from database import db 

class AlunoController():
    def index(Aluno):
        alunos = Aluno.query.order_by(Aluno.nome).all()

        resultado = []

        for aluno in alunos:
            resultado.append({
                "id": aluno.id,
                "nome": aluno.nome,
                "idade": aluno.idade,
                "email": aluno.email,
                "curso": aluno.curso,
                "ativo": aluno.ativo,
                "data_cadastro": aluno.data_cadastro.strftime("%d/%m/%Y %H:%M")
            })

        return jsonify(resultado)
    
    def listar(Aluno):

        nome = request.args.get("nome")
        curso = request.args.get("curso")
        ativo = request.args.get("ativo")

        if nome:
            alunos = Aluno.query.filter(
                Aluno.nome.like(f"%{nome}%")
            ).all()

        elif curso:
            alunos = Aluno.query.filter_by(
                curso=curso
            ).all()

        elif ativo is not None:

            if ativo.lower() == "true":
                alunos = Aluno.query.filter_by(ativo=True).all()
            else:
                alunos = Aluno.query.filter_by(ativo=False).all()

        else:
            alunos = Aluno.query.all()

        lista = []

        for aluno in alunos:
            lista.append({
                "id": aluno.id,
                "nome": aluno.nome,
                "idade": aluno.idade,
                "email": aluno.email,
                "curso": aluno.curso,
                "ativo": aluno.ativo
            })

        return jsonify(lista)
    
    def buscar(id):

        aluno = Aluno.query.get(id)

        if aluno is None:
            return jsonify({"erro": "Aluno não encontrado"}), 404

        return jsonify({
            "id": aluno.id,
            "nome": aluno.nome,
            "idade": aluno.idade,
            "email": aluno.email,
            "curso": aluno.curso,
            "ativo": aluno.ativo,
            "data_cadastro": aluno.data_cadastro.strftime("%d/%m/%Y %H:%M")
        })
        
    def cadastrar():
        dados = request.json    
        if not dados:
            return jsonify({"erro": "JSON inválido"}), 400

        if len(dados.get("nome", "")) < 3:
            return jsonify({"erro": "Nome inválido"}), 400

        idade = dados.get("idade")

        if idade is None:
            return jsonify({"erro": "Idade obrigatória"}), 400

        if idade < 5:
            return jsonify({"erro": "Idade mínima é 5 anos"}), 400

        if idade > 120:
            return jsonify({"erro": "Idade inválida"}), 400

        email = dados.get("email")

        if not email:
            return jsonify({"erro": "Email obrigatório"}), 400

        if "@" not in email:
            return jsonify({"erro": "Email inválido"}), 400

        existe = Aluno.query.filter_by(email=email).first()

        if existe:
            return jsonify({"erro": "Email já cadastrado"}), 400

        curso = dados.get("curso")

        if not curso:
            return jsonify({"erro": "Curso obrigatório"}), 400

        aluno = Aluno()

        aluno.nome = dados["nome"]
        aluno.idade = idade

        aluno.email = email
        aluno.curso = curso
        aluno.ativo = True
        db.session.add(aluno)
        db.session.commit()

        return jsonify({
            "mensagem": "Aluno cadastrado",

            "id": aluno.id
        })
        
    def atualizar(id):

        aluno = Aluno.query.get(id)

        if aluno is None:
            return jsonify({"erro": "Aluno não encontrado"}), 404

        dados = request.json

        if "nome" in dados:

            if len(dados["nome"]) < 3:
                return jsonify({"erro": "Nome inválido"}), 400

            aluno.nome = dados["nome"]

        if "idade" in dados:

            if dados["idade"] < 5:
                return jsonify({"erro": "Idade inválida"}), 400

            aluno.idade = dados["idade"]

        if "email" in dados:

            outro = Aluno.query.filter_by(
                email=dados["email"]
            ).first()

            if outro and outro.id != aluno.id:
                return jsonify({"erro": "Email já utilizado"}), 400

            aluno.email = dados["email"]

        if "curso" in dados:
            aluno.curso = dados["curso"]

        if "ativo" in dados:
            aluno.ativo = dados["ativo"]

        db.session.commit()

        return jsonify({
            "mensagem": "Aluno atualizado"
        })
        
    def excluir(id):
        aluno = Aluno.query.get(id)    
        if aluno is None:
            return jsonify({"erro": "Aluno não encontrado"}), 404        
        
        db.session.delete(aluno)
        db.session.commit()      
        return jsonify({
            "mensagem": "Aluno removido"     
        })
        
    def ativar(id):
        aluno = Aluno.query.get(id)

        if aluno is None:
            return jsonify({"erro": "Aluno não encontrado"}), 404

        aluno.ativo = True

        db.session.commit()

        return jsonify({
            "mensagem": "Aluno ativado"
        })
        
    def desativar(id):
        aluno = Aluno.query.get(id)

        if aluno is None:
            return jsonify({"erro": "Aluno não encontrado"}), 404

        aluno.ativo = False

        db.session.commit()

        return jsonify({
            "mensagem": "Aluno desativado"
        })
        
    def estatisticas():
        total = Aluno.query.count()

        ativos = Aluno.query.filter_by(
            ativo=True
        ).count()

        inativos = Aluno.query.filter_by(
            ativo=False
        ).count()

        cursos = db.session.query(
            Aluno.curso
        ).distinct().count()

        return jsonify({
            "total_alunos": total,
            "ativos": ativos,
            "inativos": inativos,
            "cursos": cursos
        })