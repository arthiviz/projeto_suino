from sqlalchemy.exc import IntegrityError
from BD.conexao import Base, SessionLocal
from models.modelPesagem import Pesagem
from datetime import datetime
from datetime import date
from flask import jsonify
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

def criar_pesagem(id,tag,peso):

    db = SessionLocal()
    data_hoje = datetime.now()

    try:
        pesagem = Pesagem(id_suino = id, tag_suino = tag, peso = peso, data_hora = data_hoje)
        adicionar = db.add(pesagem)
        db.commit()
        print('pesagem adicionada com sucesso')
        return True
        
    
    except Exception as erro:
        db.rollback()
        print(f'erro inesperado ao adicionar pesagem:{erro}')
        return False
    finally:
        db.close()

def listar_pesagem():
    db = SessionLocal()

    lista_pesagens = db.query(Pesagem).order_by(Pesagem.data_hora.desc()).all()
    for pesagem in lista_pesagens:

        pesagem.data_hora = pesagem.data_hora.strftime('%d/%m/%Y %H:%M')

    db.close()

    return lista_pesagens

def pesagens_suino(id_suino):
    db = SessionLocal()

    try:

        pesagens = db.query(Pesagem).filter(Pesagem.id_suino == id_suino).order_by(Pesagem.data_hora.desc()).all()

        resultado = []

        for pesagem in pesagens:

            resultado.append({
                "id": pesagem.id_suino,
                "data": pesagem.data_hora.isoformat() if isinstance(pesagem.data_hora, (date,)) else str(pesagem.data_hora),
                "peso": pesagem.peso
            })

        resultado = [
            {
                "id": p.id,
                "id_suino": p.id_suino,
                "tag_suino": p.tag_suino,
                "peso": p.peso,
                "data": p.data_hora.strftime("%d/%m/%Y %H:%M:%S") if p.data_hora else None
            }
            for p in pesagens
        ]

        return resultado
    
    except Exception as erro:
        db.rollback()
        print(f'erro inesperado ao buscar pesagens do suino:{erro}')
        return {"erro": str(erro)}, 500
    finally:
        db.close()

def criar_grafico(id_suino):
    db = SessionLocal()

    try:

        pesagens = db.query(Pesagem).filter(Pesagem.id_suino == id_suino).order_by(Pesagem.data_hora).all()

        if pesagens:
            df = pd.DataFrame([{"peso": p.peso,"data": p.data_hora.strftime("%d/%m/%Y <br> %H:%M:%S") } for p in pesagens])
            print(f'dataframe:{df}')

            grafico = go.Figure([go.Scatter(x=df['data'], y=df['peso'])])
            
            grafico_html = pio.to_html(grafico,full_html=False)

            return grafico_html 
            
            

        else:
            print(f'suino não encontrado para a criação do gráfico')

    except Exception as erro:
        print(f'erro inesperado na criação do gráfico:{erro}')
    finally:
        db.close()

