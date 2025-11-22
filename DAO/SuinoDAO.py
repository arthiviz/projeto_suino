from sqlalchemy.exc import IntegrityError
from BD.conexao import Base, SessionLocal
from models.modelSuino import Suino
from models.modelTag import Tag
import pandas as pd
from sqlalchemy import or_,cast,String

def criar_suino(raca,peso_inicial,tag):
    db = SessionLocal()
    try:
        
        tag_banco = db.query(Tag).filter(Tag.codigo == tag).first()

        if tag_banco:

            suino = Suino(raca = raca, peso_inicial = peso_inicial, tag = tag_banco)
            db.add(suino)
            db.commit()
            print('sucesso ao adicionar o suino')
            return True
        else:
            print('tag não encontrada ao adicionar suino')
    
    except Exception as erro:
        db.rollback()
        print(f'erro inesperado ao adicionar suino:{erro}')
        return False

    finally:
        db.close()

def remover_suino(id):
    db = SessionLocal()
    try:
        suino = db.query(Suino).filter(Suino.id == id).first()

        if not suino:
            print('id do suino nao encontrado')
            return False
        else:
            db.delete(suino)
            db.commit()
            print('suino deletado com sucesso')
            return True
    except Exception as erro:
        db.rollback()
        print(f'erro inesperado ao deletar suino:{erro}')
        return False
    finally:
        db.close()
        

def listar_suinos():
    db = SessionLocal()
    lista_suino = db.query(Suino).all()
    db.close()
    return lista_suino

def tags_livres():

    db = SessionLocal()
    tag_livre = []

    tags = db.query(Tag).all()

    for tag in tags:
        
        suino = db.query(Suino).filter(Suino.tag_suino == tag.codigo).first()
        if suino == None:
            tag_livre.append(tag)
    db.close()
    return tag_livre

def verificar_suino(tag):

    db = SessionLocal()

    suino = db.query(Suino).filter(Suino.tag_suino == tag).first()
    db.close()
    return suino

def pesquisa_suino(pesquisa):

    db = SessionLocal()

    if pesquisa:
        
        suinos = db.query(Suino) .filter(or_(cast(Suino.id, String).like(f"%{pesquisa}%"),Suino.tag_suino.like(f"%{pesquisa}%"))).all()
    else:
        suinos = db.query(Suino).all()

    db.close()

    return suinos


    