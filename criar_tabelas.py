from BD.conexao import engine, Base
from models.modelSuino import Suino
from models.modelUser import User
from models.modelTag import Tag

Tag.__table__.drop(engine, checkfirst=True)
Suino.__table__.drop(engine, checkfirst=True)
Base.metadata.drop_all(engine)
Base.metadata.create_all(bind=engine)