from models.modelUser import User
from sqlalchemy.exc import IntegrityError
from BD.conexao import SessionLocal, Base

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

        user = db.query(User).filter(nome == nome and senha == senha).first()
        
        if user:
            return True
        else:
            return False
    
    except Exception as erro:
        print(f'erro inesperado ao procurar usuario:{erro}')
        return False
    finally:
        db.close()

