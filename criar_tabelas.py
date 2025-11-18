from BD.conexao import engine, Base
from models.modelSuino import Suino
from models.modelUser import User
from models.modelTag import Tag
from models.modelPesagem import Pesagem

Base.metadata.drop_all(engine)
Base.metadata.create_all(bind=engine)