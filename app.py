from flask import *
from DAO.UserDAO import *
from DAO.SuinoDAO import *
from DAO.TagDAO import *
from DAO.PesagemDAO import *

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

@app.route('/', methods = ['POST','GET'])
def home():
    print(request.method)
    if request.method == 'POST':

        pesquisa = request.form.get('pesquisa')

        suinos_pesquisa = pesquisa_suino(pesquisa)

        

        return render_template('index.html', lista_suinos = suinos_pesquisa, active_page = 'home')
    else:
        lista_suinos = listar_suinos()
        return render_template('index.html', lista_suinos = lista_suinos, active_page = 'home')

@app.route('/registro_pessoa', methods = ['GET','POST'])
def registrar_pessoa():
    resultado = None
    if request.method == "POST":
        nome = request.form.get('nome')
        email = request.form.get('email')
        telefone = request.form.get('telefone')
        senha = request.form.get('senha')
        conf_senha = request.form.get('conf_senha')

        print(f"senha:{senha} conf_senha:{conf_senha}")

        if senha == conf_senha:
            adicionar = criar_user(nome,email,telefone,senha,)

            if adicionar:
                resultado = True
            else:
                resultado = False
        else:
            resultado = False
            
    print(f'resultado:{resultado}')
    return render_template('registro_pessoa.html', resultado = resultado, active_page = 'reg_pessoa')

@app.route('/remover_pessoa', methods=['POST','GET'])
def remover_pessoa():
    resultado = None
    if request.method == 'POST':
        

        email = request.form.get('remover-email')
        senha = request.form.get('remover-senha')

        resultado = remover_user(email,senha)

    return render_template('remover_pessoa.html',resultado = resultado, active_page = 'reg_pessoa')


@app.route('/listar_pessoa',methods = ['GET','POST'])
def lista_pessoa():

    if request.method == 'POST':
        
        pesquisa = request.form.get('pesquisa_pessoa')

        users_pesquisa = pesquisar_user(pesquisa)

        return render_template('listar_pessoas.html',users = users_pesquisa, active_page = 'reg_pessoa')

    else:

        users = listar_pessoas()

    return render_template('listar_pessoas.html',users = users, active_page = 'reg_pessoa')

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

    return render_template('registro_suino.html', tags_livres = tags_livre, resultado = resultado, active_page= 'reg_suino')

@app.route('/relatorios')
def relatorios():
    return render_template('relatorios.html')

@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect('/login')

@app.route('/registro_pesagem', methods = ['GET', 'POST'])
def registro_pesagem():
    resultado = None

    if request.method == 'POST':

        id = request.form.get('id')
        tag = request.form.get('tag')
        peso = request.form.get('peso')

        adicionar = criar_pesagem(id,tag,peso)
        print(f'valor de adicionar:{adicionar}')
        if adicionar:
            resultado = True
        else:
            resultado = False

    return render_template('registro_pesagem.html', resultado = resultado, active_page= 'reg_pesagem')

@app.route('/registro_pesagemIOT', methods = ['POST','GET'])
def registrar_pesagemIOT():

    json = request.get_json()
    if json:
        tag = json.get('tag')
        peso_suino = json.get('peso')
        print(f'\n Peso do suino:{peso_suino}')
        peso_suino = float(peso_suino)
        
        print(f'tag do suino:{tag}')

        if peso_suino is None:
            return 'Peso do suino não enviado!',400 
        

        suino = verificar_suino(tag)
        print(f'resultado:{suino}')

        if suino:

           res = criar_pesagem(suino.id,suino.tag_suino,peso_suino)

           print(f'resultado{res}')

           if res:
               print('pesagem cadastrada')
               return 'pesagem cadastrada',200
           else:
               print('erro ao registrar pesagem')
               return 'erro ao registrar pesagem',400

        else:
            print('suino não encontrado')
            return 'suino não encontrado', 400

   
        
        


@app.route('/registro_tag', methods = ['GET','POST'])
def registro_tag():
    resultado = None

    if request.method == 'POST':

        codigo = request.form.get('codigo')

        adicionar = criar_tag(codigo)

        if adicionar:
            resultado = True
        else:
            resultado = False
    
    return render_template('registro_tag.html', resultado = resultado, active_page= 'reg_tag')

@app.route('/api/buscar_pesagem/<int:suino_id>', methods = ['POST','GET'])
def buscar_pesagens(suino_id):

    pesagens = pesagens_suino(suino_id)
    graph_html = criar_grafico(suino_id)

    data = {
        "pesagens":pesagens,
        "grafico":graph_html
    }
    print(pesagens)
    return jsonify(data)

@app.route('/deletar_suino/<int:suino_id>', methods = ['GET','POST'])
def deletar_suino(suino_id):
    
    remover_suino(suino_id)

    return redirect(url_for('home'))

@app.route('/listar_pesagens')
def listar_pesagens():

    pesagens = listar_pesagem()

    return render_template('listar_pesagens.html', pesagens = pesagens, active_page = 'reg_pesagem')

@app.route('/listar_tags')
def lista_tags():

    tags = listar_tags()

    return render_template('listar_tags.html', tags = tags)



@app.before_request
def verificar_login():
    if request.path.startswith('/static/'):
        return

    rotas_livres = ['login', 'registrar_pesagemIOT']

    if request.endpoint not in rotas_livres and 'user' not in session:
        return redirect('/login')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True, port=5050)