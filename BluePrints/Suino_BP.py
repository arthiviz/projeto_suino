from flask import *
from DAO.SuinoDAO import *

suino_bp = Blueprint('suino', __name__)

@suino_bp.route('/registrar', methods = ['POST'])
def registrar():

    raca = request.form.get('raca')
    peso_inicial = request.form.get('peso_inicial')
    tag = request.form.get('tag')

    if raca != '' and peso_inicial != '' and tag != '':

        adicionar = criar_suino(raca,peso_inicial,tag)
        vazio = False
    else:
        vazio = True
        
    return render_template('registro_suino.html', resultado = adicionar, vazio = vazio)


