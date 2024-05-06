from flask import Flask, render_template, request, redirect, url_for, render_template_string 
import mysql.connector 
from user import user_app 



mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="blugin",
    password="135426@blugin",
    database="blugin_db"
    
)


#criando um objeto cursor
mycursor = mydb.cursor()

app = Flask(__name__, static_folder='static', static_url_path='/static')


@app.route('/fechar_formulario', methods=['POST'])
def fechar_formulario():

    return redirect(url_for('dashboard'))

app.register_blueprint(user_app)

@app.route('/', methods=['GET', 'POST']) #rota para logar
def index():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if authenticate(email, password):
            return redirect(url_for('dashboard'))
        else:
            return 'Invalid credentials'
    return render_template('index.html')

@app.route('/dashboard') #rota para retornar o dashboard
def dashboard():
    # Consulta para contar o número de usuários
    cursor_count = mydb.cursor()
    cursor_count.execute("SELECT COUNT(*) FROM usuario")
    total_users = cursor_count.fetchone()[0]

    # Consulta para recuperar as empresas
    mycursor.execute("SELECT idcad_empresa, cad_razao_social  FROM cad_empresa")
    companies = mycursor.fetchall()

    return render_template('dashboard.html', total_users=total_users, companies=companies)


def authenticate(email, password):
    
    return email == 'admin@blugin' and password == '123'




@app.route('/create_company', methods=['GET', 'POST'])
def create_company():
    confirmation_message = None


    if request.method == 'POST':
        # Processamento do envio do formulário
        cad_cnpj = request.form['cad_cnpj']
        cad_ie = request.form['cad_ie']
        cad_razao_social = request.form['cad_razao_social']
        cad_nome_fantasia = request.form['cad_nome_fantasia']
        cad_email = request.form['cad_email']
        cad_telefone = request.form['cad_telefone']
        cad_nome_contato = request.form['cad_nome_contato']
        cad_funcao_contato = request.form['cad_funcao_contato']
        cad_website = request.form['cad_website']
        cad_facebook = request.form['cad_facebook']
        cad_whatsapp = request.form['cad_whatsapp']
        cad_instagram = request.form['cad_instagram']
        cad_cep = request.form['cad_cep']
        cad_logradouro = request.form['cad_logradouro']
        cad_bairro = request.form['cad_bairro']
        cad_cidade = request.form['cad_cidade']
        cad_uf = request.form['cad_uf']
        cad_categoria = request.form['cad_categoria']
        cad_password_hash = request.form['cad_password_hash']
        #cad_password_salt = request.form['cad_password_salt']
        cad_observacao = request.form['cad_observacao']

        # salva a empresa no banco de dados.
        mycursor.execute("INSERT INTO cad_empresa (cad_cnpj, cad_ie, cad_razao_social, cad_nome_fantasia, cad_email, cad_telefone, cad_nome_contato, cad_funcao_contato, cad_website, cad_facebook, cad_whatsapp, cad_instagram, cad_cep, cad_logradouro, cad_bairro,cad_cidade,cad_uf,cad_categoria, cad_password_hash, cad_observacao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (cad_cnpj, cad_ie, cad_razao_social, cad_nome_fantasia, cad_email, cad_telefone, cad_nome_contato, cad_funcao_contato, cad_website, cad_facebook, cad_whatsapp, cad_instagram, cad_cep, cad_logradouro, cad_bairro,cad_cidade,cad_uf,cad_categoria, cad_password_hash, cad_observacao))
        
        
        mydb.commit()

        confirmation_message = 'Cadastro realizado com sucesso.'

        #return redirect(url_for('index'))

    return render_template('create_company.html', confirmation=confirmation_message)


@app.route('/list_company')
def list_company():
    mycursor.execute("SELECT idcad_empresa, cad_cnpj, cad_razao_social, cad_cidade, cad_uf FROM cad_empresa")
    companies = mycursor.fetchall()  # Renomeie a variável para companies
    return render_template('list_company.html', companies=companies)



@app.route('/company_details/<int:idcad_empresa>')
def company_details(idcad_empresa):
    mycursor.execute("SELECT * FROM cad_empresa WHERE idcad_empresa = %s", (idcad_empresa,))
    company_details = mycursor.fetchone()  # Usando fetchone() para obter apenas um registro
    return render_template('company_details.html', company=company_details)



@app.route('/edit_company/<int:idcad_empresa>', methods=['GET', 'POST'])
def edit_company(idcad_empresa):
    if request.method == 'POST':
        # Processar dados do formulário de edição
        cad_cnpj = request.form['cad_cnpj']
        cad_ie = request.form['cad_ie']
        cad_razao_social = request.form['cad_razao_social']
        cad_nome_fantasia = request.form['cad_nome_fantasia']
        cad_email = request.form['cad_email']
        cad_telefone = request.form['cad_telefone']
        cad_nome_contato = request.form['cad_nome_contato']
        cad_funcao_contato = request.form['cad_funcao_contato']
        cad_website = request.form['cad_website']
        cad_facebook = request.form['cad_facebook']
        cad_whatsapp = request.form['cad_whatsapp']
        cad_instagram = request.form['cad_instagram']
        cad_cep = request.form['cad_cep']
        cad_logradouro = request.form['cad_logradouro']
        cad_bairro = request.form['cad_bairro']
        cad_cidade = request.form['cad_cidade']
        cad_uf = request.form['cad_uf']
        cad_numero_contato = request.form['cad_numero_contato']
        cad_categoria = request.form['cad_categoria']
        cad_observacao = request.form['cad_observacao']
        
        # Atualizar empresa no banco de dados
        mycursor = mydb.cursor()
        sql = "UPDATE cad_empresa SET cad_cnpj = %s, cad_ie = %s, cad_razao_social = %s, cad_nome_fantasia = %s, cad_email = %s, cad_telefone = %s, cad_nome_contato = %s, cad_funcao_contato = %s, cad_website = %s, cad_facebook = %s, cad_whatsapp = %s, cad_instagram = %s, cad_cep = %s, cad_logradouro = %s, cad_bairro = %s, cad_cidade = %s, cad_uf = %s, cad_numero_contato = %s, cad_categoria = %s, cad_observacao = %s WHERE idcad_empresa = %s"
        val = (cad_cnpj, cad_ie, cad_razao_social, cad_nome_fantasia, cad_email, cad_telefone, cad_nome_contato, cad_funcao_contato, cad_website, cad_facebook, cad_whatsapp, cad_instagram, cad_cep, cad_logradouro, cad_bairro, cad_cidade, cad_uf, cad_numero_contato, cad_categoria, cad_observacao, idcad_empresa)
        mycursor.execute(sql, val)
        mydb.commit()
        
        return redirect(url_for('list_company'))
    else:
        # Recuperar dados da empresa do banco de dados com base no ID fornecido
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM cad_empresa WHERE idcad_empresa = %s", (idcad_empresa,))
        company = mycursor.fetchone()  # Assume que há apenas uma empresa com esse ID
        return render_template('edit_company.html', idcad_empresa=idcad_empresa, company=company)

@app.route('/delete_company/<int:idcad_empresa>', methods=['POST'])
def delete_company(idcad_empresa):
    # Lógica para excluir a empresa do banco de dados
    mycursor = mydb.cursor()
    sql = "DELETE FROM cad_empresa WHERE idcad_empresa = %s"
    val = (idcad_empresa,)
    mycursor.execute(sql, val)
    mydb.commit()
    
    # Redirecionar para a lista de empresas após a exclusão
    return redirect(url_for('list_company'))



#criei uma rota para listar os usuários em tela renderizando no html da página.
@app.route('/list_users')
def list_users():
    mycursor.execute("SELECT * FROM usuario")
    users = mycursor.fetchall()
    return render_template('list_users.html', users=users)

@app.route('/create_user', methods=['GET','POST'])
def create_user():
    if request.method == 'POST':
        # Lógica para criar novo usuário
        user_emp = request.form['user_emp']
        user_nome = request.form['user_nome']
        user_cpf = request.form['user_cpf']
        user_telefone = request.form['user_telefone']
        user_contato = request.form['user_contato']
        user_whatsapp = request.form['user_whatsapp']
        user_cep = request.form['user_cep']
        user_endereco = request.form['user_endereco']
        user_nr_end = request.form['user_nr_end']
        user_bairro = request.form['user_bairro']
        user_cidade = request.form['user_cidade']
        user_uf = request.form['user_uf']
        user_funcao = request.form['user_funcao']
        user_email = request.form['user_email']
        user_password = request.form['user_password']
        
        # Executar a inserção no banco de dados
        sql = "INSERT INTO usuario (user_emp, user_nome, user_cpf, user_telefone, user_contato, user_whatsapp, user_cep, user_endereco, user_nr_end, user_bairro, user_cidade, user_uf, user_funcao, user_email, user_password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (user_emp, user_nome, user_cpf, user_telefone, user_contato, user_whatsapp, user_cep, user_endereco, user_nr_end, user_bairro, user_cidade, user_uf, user_funcao, user_email, user_password)
        mycursor.execute(sql, val)
        mydb.commit()
        
        return redirect(url_for('list_users'))
    return render_template('create_user.html')


@app.route('/edit_user/<int:idusuario>', methods=['GET', 'POST'])
def edit_user(idusuario):
    if request.method == 'POST':
        # Processar dados do formulário de edição
        user_emp = request.form['user_emp']
        user_nome = request.form['user_nome']
        user_cpf = request.form['user_cpf']
        user_telefone = request.form['user_telefone']
        user_contato = request.form['user_contato']
        user_whatsapp = request.form['user_whatsapp']
        user_cep = request.form['user_cep']
        user_endereco = request.form['user_endereco']
        user_nr_end = request.form['user_nr_end']
        user_bairro = request.form['user_bairro']
        user_cidade = request.form['user_cidade']
        user_uf = request.form['user_uf']
        user_funcao = request.form['user_funcao']
        user_email = request.form['user_email']
        
        # Atualizar usuário no banco de dados
        mycursor = mydb.cursor()
        sql = "UPDATE usuario SET user_emp = %s, user_nome = %s, user_cpf = %s, user_telefone = %s, user_contato = %s, user_whatsapp = %s, user_cep = %s, user_endereco = %s, user_nr_end = %s, user_bairro = %s, user_cidade = %s, user_uf = %s, user_funcao = %s, user_email = %s WHERE idusuario = %s"
        val = (user_emp, user_nome, user_cpf, user_telefone, user_contato, user_whatsapp, user_cep, user_endereco, user_nr_end, user_bairro, user_cidade, user_uf, user_funcao, user_email, idusuario)
        mycursor.execute(sql, val)
        mydb.commit()
        
        return redirect(url_for('list_users'))
    else:
        # Recuperar dados do usuário do banco de dados com base no ID fornecido
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM usuario WHERE idusuario = %s", (idusuario,))
        user = mycursor.fetchone()  # Assume que há apenas um usuário com esse ID
        return render_template('edit_user.html', idusuario=idusuario, user=user)

@app.route('/delete_user/<int:idusuario>', methods=['POST'])
def delete_user(idusuario):
    mycursor = mydb.cursor()
    mycursor.execute("DELETE FROM usuario WHERE idusuario = %s", (idusuario,))
    mydb.commit()

    # Redirecionar de volta para a lista de usuários após a exclusão
    return redirect(url_for('list_users'))

@app.route('/list_category')
def list_category():
    mycursor.execute("SELECT idcategoria, nome_cat, descricao_cat FROM categoria")
    categories = mycursor.fetchall()
    return render_template('list_category.html', categories=categories)

@app.route('/create_category', methods=['POST','GET'])
def create_category():
    if request.method == 'POST':
        nome_categoria = request.form['category_name']
        descricao_categoria = request.form['category_description']
        
        mycursor.execute("INSERT INTO categoria (nome_cat, descricao_cat) VALUES (%s, %s)", (nome_categoria, descricao_categoria))
        mydb.commit()

        return redirect(url_for('list_category'))        
    return render_template('create_user.html')


if __name__ == '__main__':
    app.run(debug=True)
