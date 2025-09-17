from sqlalchemy import create_engine,text
from sqlalchemy.orm import sessionmaker, declarative_base


usuario = 'root'
senha = ''
bd = 'sistema_suino'
porta = 3306


DATABASE_URL = f"mysql+pymysql://{usuario}:{senha}@localhost:{porta}/{bd}"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def testar_conexao():
    try:
        with engine.connect() as conn:
            conn.execute (text("SELECT 1"))  # comando simples
            print(" Conexão bem-sucedida com o banco!")
    except Exception as e:
        print(" Erro na conexão:", e)


if __name__ == "__main__":
    testar_conexao()