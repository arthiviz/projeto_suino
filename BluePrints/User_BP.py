from flask import *
from DAO.UserDAO import *

user_bp = Blueprint('user',__name__)

@user_bp.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        nome = request.form.get('nome')
        senha = request.form.get('senha')

        if nome != '' and senha != '':

            if login(nome,senha):
                return redirect('/')
            else:
                return redirect('/')
       
@user_bp.route('/')
def home():
    return 'oi'