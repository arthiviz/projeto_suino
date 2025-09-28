from BD.conexao import Base
from sqlalchemy import *
from sqlalchemy.orm import relationship

class Suino(Base):

    __tablename__ = 'suino'
    
    id = Column(Integer, index = True , primary_key=True)
    raca = Column(String(50), nullable=False)
    peso_inicial = Column(DECIMAL(7,2), nullable=False)
    peso_atual = Column(DECIMAL(7,2))
    tag_suino = Column(ForeignKey("tag.codigo", ondelete="CASCADE"), unique=True)
    tag = relationship("Tag", back_populates="suino", uselist=False)

