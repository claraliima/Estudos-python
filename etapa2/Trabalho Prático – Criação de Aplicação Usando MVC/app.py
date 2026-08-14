from database import db 
from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SECRET_KEY'] = 'clara'

db.init_app(app)

#app.register_blueprint()
from models import *
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run()