import dados

# flask = biblioteca | Flask = classe da biblioteca
from flask import Flask, jsonify, request

biblioteca = dados.carregar_do_arquivo()


app = Flask(__name__)

@app.route("/livros", methods=["GET", "POST"])
def livros():
    if request.method == 'GET':
        return jsonify(biblioteca) # jsonify -> converte objeto PY para JSON -> p/retornar corpo requisição
    if request.method == 'POST':
        novo = request.get_json()
        biblioteca.append(novo)
        dados.salvar_no_arquivo(biblioteca)
        return "Livro criado, 201"

#duvida
@app.route("/livros/<isbn>", methods=["GET", "PUT", "DELETE"])
def livros_isbn(isbn = None): 
    if request.method == 'GET':   
        livro_encontrado = None
        for livro in biblioteca:
            if livro['isbn'] == isbn:
                livro_encontrado = jsonify(livro)
                return "Livro encontrado, 200"
        else:
            return 'Livro não encontrado, 404'   
    if request.method == 'PUT':
        livro_encontrado = None

        #Passa por cada livro no arquivo
        for livro in biblioteca:
            #Se o isbn do livro estiver no arquivo
            if livro['isbn'] == isbn:
                livro_encontrado = livro
                # Pega os novos dados enviados no corpo da requisição
                novos_dados = request.get_json()
                # Atualiza apenas os campos que foram enviados
                for campo, valor in novos_dados.items():
                    if campo in livro_encontrado:
                        livro_encontrado[campo] = valor
                        dados.salvar_no_arquivo(biblioteca)
                        return 'Livro alterado, 200'

        if not livro_encontrado:
            return 'Livro não encontrado, 404' 
    if request.method == 'DELETE':
        if isbn:
            for livro in biblioteca:
                if livro['isbn'] == isbn :
                    biblioteca.remove(livro)
                    dados.salvar_no_arquivo(biblioteca)
                    return 'Livro apagado, 200'
            else: 
                return  'Nenhum livro encontrado, 404'
        else:
            return 'Solicitação inválida' 


if __name__ == "__main__":
    app.run(debug = True)
