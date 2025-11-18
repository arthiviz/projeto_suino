from sqlalchemy.exc import IntegrityError
from BD.conexao import Base, SessionLocal
from models.modelPesagem import Pesagem
import pandas as pd
import plotly.graph_objects as go

def criar_grafico(id_suino):
    db = SessionLocal()

    try:

        pesagens = db.query(Pesagem).filter(Pesagem.id_suino == id_suino).order_by(Pesagem.data_hora).all()

        if pesagens:
            df = pd.DataFrame([{"peso": p.peso,"data": p.data_hora.strftime("%d/%m/%Y <br> %H:%M:%S") } for p in pesagens])
            print(f'dataframe:{df}')

            grafico = go.Figure([go.Scatter(x=df['data'], y=df['peso'])])
            grafico.show()
            
            return grafico
            
            

        else:
            print(f'suino não encontrado para a criação do gráfico')

    except Exception as erro:
        print(f'erro inesperado na criação do gráfico:{erro}')
    finally:
        db.close()


criar_grafico(1)