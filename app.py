from flask import *
from DAO.UserDAO import *
from DAO.SuinoDAO import *
from DAO.TagDAO import *

app = Flask(__name__)
app.secret_key = 'abcd1234'

@app.route("/login", methods = ['GET','POST'])
def login():
    print(f'metodo:{request.method}')
    if request.method == 'POST':
        nome = request.form.get("nome")
        senha = request.form.get("senha")

        print(f'nome:{nome}, senha:{senha}')

        login = login_user(nome,senha)
        print(f'resultado{login}')

        if login:
            session['user'] = nome
            return redirect('/')

    return render_template('login.html')

@app.route('/')
def home():

    
    lista_suinos = listar_suinos()
    return render_template('index.html', lista_suinos = lista_suinos)

@app.route('/registro_pessoa', methods = ['GET','POST'])
def registrar_pessoa():
    resultado = None
    if request.method == "POST":
        nome = request.form.get('nome')
        email = request.form.get('email')
        telefone = request.form.get('telefone')
        senha = request.form.get('senha')
        conf_senha = request.form.get('conf_senha')

        if senha == conf_senha:
            adicionar = criar_user(nome,email,telefone,senha,)

            if adicionar:
                resultado = True
            else:
                resultado = False
        else:
            resultado = False
            

    return render_template('registro_pessoa.html', resultado = resultado)

@app.route('/registro_suino', methods = ['GET','POST'])
def registrar_suino():
    resultado = None
    
    if request.method == 'POST':

        raca = request.form.get('raca')
        peso_inicial = request.form.get('peso_inicial')
        tag = request.form.get('tag')

        adicionar = criar_suino(raca,peso_inicial,tag)
        if adicionar:
            resultado = True
        else:
            resultado = False

    
    tags_livre = tags_livres()
    print(f'tags livres{tags_livre}')

    return render_template('registro_suino.html', tags_livres = tags_livre, resultado = resultado)

@app.route('/remover_suino')
def remover_suino():
    return render_template('remover_suino.html')

@app.route('/relatorios')
def relatorios():
    return render_template('relatorios.html')

@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect('/login')


@app.before_request
def verificar_login():
    if request.endpoint != 'login' and 'user' not in session:
        return redirect('/login')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True, port=5000)