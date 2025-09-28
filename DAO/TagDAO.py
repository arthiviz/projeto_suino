from models.modelTag import Tag
from BD.conexao import Base,SessionLocal

def listar_tags():
    db = SessionLocal()

    tags = db.query(Tag).all()

    return tags

def criar_tag(tag_valor):
    db = SessionLocal()

    try:
        tag = Tag(codigo = tag_valor)
        db.add(tag)
        db.commit()
        print('sucesso ao adicionar tag')
        return True
    except Exception as erro:
        db.rollback()
        print(f'erro inesperado ao adicionar tag:{erro}')
        return False
    finally:
        db.close()




