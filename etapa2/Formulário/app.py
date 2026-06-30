import dados
from flask import Flask, jsonify, request, render_template, redirect, url_for

biblioteca = dados.carregar_do_arquivo()
app = Flask(__name__)


@app.route("/", methods=["GET"])
def renderizar():
    return render_template("tabela.html", biblioteca=biblioteca)


@app.route("/biblioteca/criar", methods=["GET", "POST"])
def criar_web():
    if request.method == "GET":
        return render_template("criar_livro.html")

    isbn = request.form.get('isbn')
    if any(l['isbn'] == isbn for l in biblioteca):
        return jsonify("Livro já está cadastrado"), 409

    biblioteca.append(request.form.to_dict())
    dados.salvar_no_arquivo(biblioteca)
    return redirect(url_for("renderizar"))


@app.route("/biblioteca/atualizar", methods=["GET", "POST"])
def atualizar_web():
    if request.method == "GET":
        isbn = request.args.get("isbn")
        for l in biblioteca:
            if l["isbn"] == isbn:
                return render_template("alterar_livro.html", livro=l)
        return "Livro não encontrado", 404
    else:
        isbn = request.form.get('isbn')
        for i, l in enumerate(biblioteca):
            if l['isbn'] == isbn:
                biblioteca[i] = request.form.to_dict()
                dados.salvar_no_arquivo(biblioteca)
                return redirect(url_for("renderizar"))

        return "Livro não encontrado", 404


if __name__ == "__main__":
    app.run(debug=True)