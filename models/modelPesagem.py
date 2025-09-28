from sqlalchemy import *
from BD.conexao import Base, SessionLocal

class Pesagem(Base):

    __tablename__ = 'pesagem'

    id = Column(Integer, index=True, primary_key=True)
    id_suino = Column(ForeignKey("suino.id"), nullable=True)
    tag_suino = Column(String(20), nullable=True)
    peso = Column(DECIMAL(7,2), nullable=True)
    data_hora = Column(DateTime, nullable=True)



def to_dict(self):
        return {
            "id": self.id,
            "id_suino": self.id_suino,
            "tag_suino": self.tag_suino,
            "peso": self.peso,
            "data_hora": self.data_hora.strftime("%Y-%m-%d %H:%M:%S") if self.data_hora else None
        }