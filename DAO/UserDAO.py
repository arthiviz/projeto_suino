from models.modelUser import User
from sqlalchemy.exc import IntegrityError
from BD.conexao import SessionLocal, Base
from sqlalchemy import or_

def criar_user(nome,email,telefone,senha):

    db = SessionLocal()

    try:
        
        user = User(nome=nome,email=email,telefone=telefone,senha=senha)

        db.add(user)
        db.commit()

        print('usuario adicionado com sucesso')

        return True
    
    except Exception as erro:
        db.rollback()
        print(f'erro inesperado{erro}')

    
    finally:
        db.close()


def login_user(nome,senha):
    db = SessionLocal()
    try:

        user = db.query(User).filter(User.nome == nome, User.senha == senha).first()
        print(f'usuario:{user.nome},senha:{user.senha}')
        if user:
            return True
        else:
            return False
    
    except Exception as erro:
        print(f'erro inesperado ao procurar usuario:{erro}')
        return False
    finally:
        db.close()


def remover_user(email, senha):
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.email == email, User.senha == senha).first()

        if not user:
            return False

        db.delete(user)
        db.commit()
        print('Usuário removido com sucesso')
        return True

    except Exception as erro:
        db.rollback()
        print(f'Erro inesperado ao deletar usuário: {erro}')
        return False

    finally:
        db.close()

    

def buscar_pessoa(email):

    db = SessionLocal()

    user = db.query(User).filter(User.email == email).first()
    db.close()

    if user:
        return True
    else:
        return False
    

def listar_pessoas():

    db = SessionLocal()

    user = []

    users = db.query(User).all()
    db.close()

    return users

def pesquisar_user(pesquisa):

    db = SessionLocal()

    if pesquisa:
        users = db.query(User) .filter(or_(User.nome.like(f"%{pesquisa}%"),User.email.like(f"%{pesquisa}%"))).all()
    else:
        users = db.query(User).all()

    db.close()
    
    return users
