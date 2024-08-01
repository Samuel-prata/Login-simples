from flask import render_template, request
from model import User, db

def init_route(app):
    
    @app.route('/login')
    def logar():
        return render_template('login.html')
    
    @app.route('/registrar', methods=['POST',])
    def registrar():
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        users = User(nome, email, senha)
        db.session.add(users)
        db.session.commit()

        return 'Dados atualizados com sucesso'