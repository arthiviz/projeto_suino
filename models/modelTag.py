from BD.conexao import Base
from .modelSuino import Suino
from sqlalchemy import *
from sqlalchemy.orm import relationship


class Tag(Base):

    __tablename__ = 'tag'

    codigo = Column(String(20), primary_key=True, nullable=True)
    suino = relationship("Suino", back_populates="tag")
