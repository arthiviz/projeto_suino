from models.modelTag import Tag
from BD.conexao import Base,SessionLocal

def listar_tags():
    db = SessionLocal()

    tags = db.query(Tag).all()

    return tags


