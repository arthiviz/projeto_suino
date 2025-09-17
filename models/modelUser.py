from BD.conexao import Base
from sqlalchemy import *

class User(Base):

    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    telefone =  Column(String(20), unique=True, nullable=False)
    senha = Column(String(50), nullable=False)