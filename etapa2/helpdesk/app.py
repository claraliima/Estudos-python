from database import db
from flask import Flask, jsonify

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SECRET_KEY'] = 'clara'

db.init_app(app)

from models import *
from routes import usuario_bp, chamado_bp

app.register_blueprint(usuario_bp)
app.register_blueprint(chamado_bp)

with app.app_context():
    db.create_all()


@app.errorhandler(404)
def nao_encontrado(e):
    return jsonify({"erro": "Recurso não encontrado."}), 404


if __name__ == "__main__":
    app.run(debug=True)
