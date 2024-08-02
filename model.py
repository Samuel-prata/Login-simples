from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__='usuario'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    tel = db.Column(db.String(20))
    empresa = db.Column(db.String(100))
    senha = db.Column(db.String(100))

    def __init__(self, nome, email, tel, empresa, senha):
        self.nome = nome
        self.email = email
        self.tel = tel
        self.empresa = empresa
        self.senha = senha

        