from flask import Flask
from database import db
from routers.aluno_route import aluno_bp

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///escola.db"
app.config["SECRET_KEY"] = 'minhachavesupersecretaqueninguemvaidescobrir'

with app.app_context():
    db.create_all()
    
app.register_blueprint(aluno_bp)
    
if __name__ == "__main__":
    app.run(debug=True)