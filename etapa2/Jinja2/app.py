import dados

# flask = biblioteca | Flask = classe da biblioteca
from flask import Flask, jsonify, request, render_template, redirect, url_for

biblioteca = dados.carregar_do_arquivo()

app = Flask(__name__)


@app.route("/", methods=["GET"])
def renderizar():
    return render_template("index.html", biblioteca=biblioteca)

@app.route("/biblioteca/criar", methods=["GET", "POST"])
def criar_web():
    if request.method == "POST":
        novo_livro = {
                    'isbn': request.form.get('isbn'),
                    'titulo': request.form.get('titulo'),
                    'autor': request.form.get('autor'),
                    "genero": request.form.get('genero'),
                    "ano_publicacao": request.form.get('ano_publicacao'),
                    "editora": request.form.get('editora'),
                    "paginas": request.form.get('paginas'),
                    "status": request.form.get('status'),
                    "localizacao": request.form.get('localizacao')
                }
        for l in biblioteca:
            if l['isbn'] == novo_livro['isbn']:
                return jsonify("Livro já está cadastrado")

        biblioteca.append(novo_livro)
        dados.salvar_no_arquivo(biblioteca)
        return redirect(url_for("renderizar"))

    else:
        return render_template("criar_livro")

    
if __name__ == "__main__":
    app.run(debug = True)