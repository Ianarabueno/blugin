from flask import Blueprint, render_template, request, redirect, url_for

user_app = Blueprint('user_app', __name__)

@user_app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Obtenha os dados do formulário de registro
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Adicione seu código para registrar o usuário aqui

        return redirect(url_for('login'))

    # Se a requisição for GET, renderize o formulário de registro
    return render_template('register.html')

@user_app.route('/login')
def login():
    return render_template('login.html')

# Exporte o blueprint para que possa ser importado no arquivo principal do Flask
export_user_app = user_app