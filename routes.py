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
        tel = request.form['empresa']
        empresa = request.form['tel']
        senha = request.form['senha']
        users = User(nome=nome, email=email, empresa=empresa, tel=tel, senha=senha)
        db.session.add(users)
        db.session.commit()

        return 'Dados registrados com sucesso'
    
    @app.route('/busca', methods=['GET'])
    def buscar_dados():
        db.Query.session.get()